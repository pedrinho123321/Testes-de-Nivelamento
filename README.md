# Teste 1 - Web Scraping - Pedro Vilas Boas Vasconcelos

Este repositório contém a resolução do **Teste 1** do processo seletivo para a vaga de estágio na **IntuitiveCare**. O objetivo desta etapa foi desenvolver um código para:

1. **Acessar o site** da **ANS (Agência Nacional de Saúde Suplementar)**.
2. **Identificar e baixar** os arquivos **Anexo I** e **Anexo II** em formato **PDF**.
3. **Compactar** os arquivos baixados em um **arquivo ZIP**.

## 🖥️ Descrição do Código

A solução foi implementada em **Python** e utiliza as bibliotecas `urllib` e `HTMLParser` para realizar **web scraping**, identificar os links corretos e baixar os arquivos PDF do site da **ANS**. O fluxo do código segue as seguintes etapas:

### 🚀 Etapas do Processo

1. **Acesso ao Site**:  
   - O script acessa a URL do site da **ANS** e obtém o conteúdo da página.

2. **Identificação dos Links de PDF**:  
   - O código analisa a estrutura HTML da página e extrai os links correspondentes aos arquivos **Anexo I** e **Anexo II**.

3. **Download dos Arquivos PDF**:  
   - Utilizando `urllib`, o script realiza o download dos PDFs e os salva localmente.

4. **Compactação dos Arquivos**:  
   - Os arquivos baixados são compactados em um **arquivo ZIP**, garantindo melhor organização e portabilidade.

---

## 📌 Execução

Para executar o código e realizar o processo de **Web Scraping**, siga os passos abaixo:

### 1. Instalar Dependências

O código requer as bibliotecas **`urllib`** e **`HTMLParser`** para fazer o download dos PDFs e realizar o scraping do conteúdo da página. Você pode instalar as dependências necessárias

### 2. Executar o Script

Após instalar as dependências, basta rodar o script. O programa irá:

- **Acessar o site da ANS**.
- **Identificar os links** para os arquivos PDF dos Anexos I e II.
- **Realizar o download** desses arquivos.
- **Compactar os arquivos baixados** em um único arquivo ZIP.
