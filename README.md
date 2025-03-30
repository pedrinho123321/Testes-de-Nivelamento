# Teste 3 - Banco de Dados - Pedro Vilas Boas Vasconcelos

Este repositório contém a resolução do Teste 3 do processo seletivo para a vaga de estágio na IntuitiveCare. O objetivo desta etapa é desenvolver scripts SQL para:

- Baixar arquivos de demonstrações contábeis dos últimos 2 anos do repositório público da ANS.
- Baixar os dados cadastrais das operadoras ativas na ANS no formato CSV.
- Criar queries para estruturar tabelas necessárias para armazenar os dados do arquivo CSV.
- Elaborar queries para importar os dados para o banco de dados, garantindo o encoding correto.

## 📌 Etapas do Processo

### 1️⃣ Download dos Arquivos

Os arquivos necessários para este teste estão disponíveis nos seguintes links:

- [Demonstrações Contábeis - Últimos 2 anos](https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/)
- [Dados Cadastrais das Operadoras Ativas na ANS](https://dadosabertos.ans.gov.br/FTP/PDA/operadoras_de_plano_de_saude_ativas/)

### 2️⃣ Criação da Estrutura do Banco de Dados

Os scripts SQL criam as tabelas necessárias para armazenar os dados extraídos. As tabelas foram estruturadas para garantir integridade e eficiência na consulta dos dados.

### 3️⃣ Importação dos Dados

As queries foram elaboradas para importar corretamente os dados baixados, garantindo que o encoding dos arquivos esteja adequado (é recomendado UTF-8 para evitar problemas com caracteres especiais).

## 🚀 Execução dos Scripts

Para executar os scripts SQL, siga os passos abaixo:

1. Certifique-se de ter um banco de dados MySQL 8+ ou PostgreSQL 10+ configurado.
2. Execute os scripts de criação das tabelas.
3. Baixe os arquivos da ANS e ajuste os caminhos nos scripts de importação.
4. Execute os scripts de importação para carregar os dados no banco.

Caso tenha dúvidas, entre em contato! 😊

