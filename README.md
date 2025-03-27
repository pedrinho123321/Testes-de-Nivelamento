# Teste 1 - Web Scraping - Pedro Vilas Boas Vasconcelos

Este repositório contém a resolução do **Teste 1** do processo seletivo para a vaga de estágio na **IntuitiveCare**. A tarefa consistia em desenvolver um código para:

1. Acessar o site da ANS (Agência Nacional de Saúde Suplementar).
2. Realizar o download dos **Anexos I e II** em formato PDF.
3. Compactar os arquivos PDF em um único arquivo ZIP.

## Descrição do Código

A solução foi implementada em **Python** e usa a biblioteca `HTMLParser` para realizar o **web scraping** e identificar os links para os arquivos PDF no site da ANS. Além disso, foi utilizado o módulo `urllib` para realizar o download dos PDFs e a biblioteca `zipfile` para compactar os arquivos.

### Etapas do Processo

1. **Acesso ao Site**: O script acessa a URL do site da ANS e obtém o conteúdo da página.
2. **Identificação dos Links de PDF**: O código analisa a página HTML e extrai todos os links que levam a arquivos PDF.
3. **Download dos Arquivos PDF**: O código faz o download dos arquivos que contenham "Anexo I" e "Anexo II" no nome.
4. **Compactação dos Arquivos**: Os PDFs baixados são compactados em um único arquivo ZIP para facilitar o envio e armazenamento.
