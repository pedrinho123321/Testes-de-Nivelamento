# Teste 2 - Transformação de Dados - Pedro Vilas Boas Vasconcelos

Este repositório contém a resolução do **Teste 2** do processo seletivo para a vaga de estágio na **IntuitiveCare**. O objetivo desta etapa foi desenvolver um código para:

1. **Extrair dados** da tabela **"Rol de Procedimentos e Eventos em Saúde"** contida no **Anexo I** (obtido no Teste 1).
2. **Transformar os dados**, substituindo abreviações específicas por suas descrições completas.
3. **Exportar os dados** transformados para um arquivo **CSV**.
4. **Compactar** o arquivo CSV gerado em um **arquivo ZIP** para facilitar o armazenamento e envio.

## 🖥️ Descrição do Código

A solução foi implementada em **Python** e utiliza as bibliotecas `tabula-py`, `pandas` e `PyPDF2` para processar o **Anexo I** em PDF. O fluxo do código segue as seguintes etapas:

### 🚀 Etapas do Processo

1. **Leitura do PDF**:  
   - O script acessa o **Anexo I** e extrai a tabela de interesse utilizando a biblioteca `tabula-py`.

2. **Transformação dos Dados**:  
   - As colunas **"OD"** e **"AMB"** contêm abreviações que são substituídas por suas descrições completas, conforme a legenda do documento.

3. **Exportação para CSV**:  
   - Após a transformação, os dados são organizados e salvos em um arquivo **CSV** utilizando a biblioteca `pandas`.

4. **Compactação do Arquivo**:  
   - O arquivo CSV gerado é compactado em um **arquivo ZIP**, garantindo melhor organização e portabilidade.

---

## 📌 Execução

Para rodar o script referente à segunda questão, siga os passos abaixo:

### Instalar Dependências  

O código depende das bibliotecas `tabula-py`, `pandas` e `PyPDF2`. Para instalar as dependências necessárias, execute o comando abaixo:

### 1. Baixar o Anexo I
Antes de rodar o script da segunda questão, execute o script da primeira questão para baixar o Anexo I em PDF.

### 2. Executar o Script
Após instalar as dependências e baixar o PDF do Anexo I, basta rodar o script. O programa irá:

- Extrair os dados da tabela do Anexo I.
- Substituir as abreviações nas colunas "OD" e "AMB".
- Salvar os dados em formato CSV.
- Compactar o CSV em um arquivo ZIP.
