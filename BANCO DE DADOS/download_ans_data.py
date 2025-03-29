import requests
import os

def download_file(url, local_filename):
    print(f"Baixando {url}")
    response = requests.get(url, stream=True)
    response.raise_for_status()
    
    with open(local_filename, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)
    return local_filename

def get_ans_files():
    """Retorna os links dos arquivos de 2023 e 2024."""
    base_url = "https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/"
    years = ["2023", "2024"]
    quarters = ["1T", "2T", "3T", "4T"]

    files_to_download = []
    for year in years:
        for quarter in quarters:
            file_url = f"{base_url}{year}/{quarter}{year}.zip"
            files_to_download.append(file_url)

    return files_to_download

def main():
    # Cria diretório de dados
    if not os.path.exists('data'):
        os.makedirs('data')
    
    # Baixa arquivos de demonstracoes contabeis
    print("Baixando arquivos de demonstracoes contabeis...")
    files = get_ans_files()
    downloaded_files = []
    for file_url in files:
        try:
            filename = os.path.join('data', os.path.basename(file_url))
            download_file(file_url, filename)
            downloaded_files.append(os.path.basename(filename))
        except requests.exceptions.RequestException as e:
            print(f"Erro ao baixar {file_url}: {e}")
    
    # Baixa CSV de operadoras ativas (URL corrigida)
    print("\nBaixando CSV de operadoras ativas...")
    operadoras_url = "https://dadosabertos.ans.gov.br/FTP/PDA/operadoras_de_plano_de_saude_ativas/Relatorio_cadop.csv"
    operadoras_file = os.path.join('data', 'operadoras_ativas.csv')
    try:
        download_file(operadoras_url, operadoras_file)
    except requests.exceptions.RequestException as e:
        print(f"Erro ao baixar arquivo de operadoras: {e}")
    
    print("\nDownload concluído!")
    print("\nArquivos de demonstracoes contabeis baixados:")
    for file in downloaded_files:
        print(f"- {file}")
    print("\nArquivos de de operadoras ativas baixados:")
    print(f"- {operadoras_file}")

if __name__ == "__main__":
    main()
