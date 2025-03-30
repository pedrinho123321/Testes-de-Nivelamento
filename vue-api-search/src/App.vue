<template>
  <div class="container">
    <h1>Busca de Operadoras ANS</h1>

    <div class="search-box">
      <input
        type="text"
        v-model="searchQuery"
        @input="searchOperadoras"
        placeholder="Digite para buscar operadoras..."
      />
    </div>

    <div class="results" v-if="operadoras.length > 0">
      <div
        class="operadora-card"
        v-for="operadora in operadoras"
        :key="operadora.registro_ans"
      >
        <h3>{{ operadora.razao_social }}</h3>
        <p><strong>Nome Fantasia:</strong> {{ operadora.nome_fantasia }}</p>
        <p><strong>Registro ANS:</strong> {{ operadora.registro_ans }}</p>
        <p><strong>CNPJ:</strong> {{ operadora.cnpj }}</p>
        <p><strong>Modalidade:</strong> {{ operadora.modalidade }}</p>
      </div>
    </div>

    <div class="no-results" v-else-if="searchQuery">
      Nenhuma operadora encontrada.
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      searchQuery: "",
      operadoras: [],
      timeout: null,
    };
  },
  methods: {
    async searchOperadoras() {
      // Debounce para evitar muitas requisições
      clearTimeout(this.timeout);
      this.timeout = setTimeout(async () => {
        if (this.searchQuery.length >= 2) {
          try {
            const response = await fetch(
              `http://localhost:8000/api/operadoras/busca?q=${encodeURIComponent(
                this.searchQuery
              )}`
            );
            const data = await response.json();
            this.operadoras = data.operadoras;
          } catch (error) {
            console.error("Erro na busca:", error);
          }
        } else {
          this.operadoras = [];
        }
      }, 300);
    },
  },
};
</script>

<style>
.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}

h1 {
  text-align: center;
  color: #2c3e50;
  margin-bottom: 30px;
}

.search-box {
  margin-bottom: 20px;
}

input {
  width: 100%;
  padding: 12px;
  font-size: 16px;
  border: 2px solid #ddd;
  border-radius: 8px;
  outline: none;
}

input:focus {
  border-color: #3498db;
}

.operadora-card {
  background: white;
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 15px;
  margin-bottom: 15px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.operadora-card h3 {
  margin: 0 0 10px 0;
  color: #2c3e50;
}

.operadora-card p {
  margin: 5px 0;
  color: #34495e;
}

.no-results {
  text-align: center;
  color: #7f8c8d;
  padding: 20px;
}
</style>
