# Teste 4 - API e Interface Web - Pedro Vilas Boas Vasconcelos

Este repositório contém a resolução do Teste 4 do processo seletivo para a vaga de estágio na IntuitiveCare. O objetivo desta etapa é desenvolver uma API para busca de operadoras de planos de saúde e criar uma interface web interativa para consulta desses dados.

## 📌 Etapas do Processo

### 1️⃣ Download dos Arquivos

Os dados necessários para esta etapa foram obtidos do link:

- [Dados Cadastrais das Operadoras Ativas na ANS](https://dadosabertos.ans.gov.br/FTP/PDA/operadoras_de_plano_de_saude_ativas/)

### 2️⃣ Desenvolvimento do Servidor FastAPI

O servidor foi desenvolvido utilizando FastAPI para fornecer uma API de busca textual nas operadoras de planos de saúde. As principais funcionalidades incluem:

- **Endpoint de busca**: permite realizar consultas textuais e retorna os registros mais relevantes.
- **Carregamento de dados**: leitura do arquivo CSV e armazenamento dos dados para consultas rápidas.

### 3️⃣ Criação da Interface Web com Vue.js

Foi desenvolvida uma interface web usando Vue.js para interagir com a API, permitindo que os usuários realizem buscas de forma dinâmica e intuitiva.

### 4️⃣ Coleção do Postman

Para validar a API, foi elaborada uma coleção no Postman que demonstra o funcionamento da busca e os possíveis retornos.

## 🚀 Como Executar

### Banco de Dados e API:

1. **Instalar dependências**:
   ```bash
   pip install fastapi uvicorn pandas
   ```
2. **Executar o servidor FastAPI**:
   ```bash
   uvicorn main:app --reload
   ```
3. **Acessar a documentação interativa da API**:
   - [http://localhost:8000/docs](http://localhost:8000/docs)

### Interface Web:

1. **Instalar dependências do Vue.js**:
   ```bash
   npm install
   ```
2. **Iniciar o frontend**:
   ```bash
   npm run dev
   ```
3. **Acessar a aplicação web no navegador**.

Caso tenha dúvidas, entre em contato! 😊

