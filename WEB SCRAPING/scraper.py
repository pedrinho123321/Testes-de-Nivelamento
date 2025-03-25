# Pedro Vilas Boas Vasconcelos
# TESTES DE NIVELAMENTO - Intuitive Care
# Teste 1 - Web Scraper
# linguagem usa Python

import urllib.request
import urllib.error
from html.parser import HTMLParser
import zipfile
import os
import re

class ANSParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.pdf_links = []
        
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for attr in attrs:
                if attr[0] == 'href':
                    href = attr[1]
                    if '.pdf' in href.lower():
                        # Ensure full URL
                        if not href.startswith('http'):
                            href = 'https://www.gov.br' + href
                        print(f"Found PDF link: {href}")
                        self.pdf_links.append(href)

def download_pdf(url, filename):
    try:
        print(f"Attempting to download from: {url}")
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        request = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(request) as response:
            with open(filename, 'wb') as f:
                f.write(response.read())
        print(f"Successfully downloaded: {filename}")
        return True
    except Exception as e:
        print(f"Error downloading {filename}: {str(e)}")
        return False

def create_zip(pdf_files, zip_name):
    try:
        with zipfile.ZipFile(zip_name, 'w') as zipf:
            for pdf in pdf_files:
                if os.path.exists(pdf):
                    zipf.write(pdf)
                    print(f"Added {pdf} to zip file")
        print(f"Created zip file: {zip_name}")
    except Exception as e:
        print(f"Error creating zip file: {str(e)}")

def main():
    print("Starting web scraper...")
    
    # Create directory for anexos if it doesn't exist
    if not os.path.exists('anexos'):
        os.makedirs('anexos')
        print("Created anexos directory")

    # URL of the target page
    url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
    print(f"Accessing URL: {url}")
    
    try:
        # Get the page content
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        request = urllib.request.Request(url, headers=headers)
        response = urllib.request.urlopen(request)
        html_content = response.read().decode('utf-8')
        print("Successfully retrieved page content")
        
        # Parse HTML content
        parser = ANSParser()
        parser.feed(html_content)
        print(f"Found {len(parser.pdf_links)} PDF links in total")
        
        # Download PDFs containing "Anexo I" and "Anexo II"
        pdf_files = []
        for href in parser.pdf_links:
            # Check for the specific Anexo PDFs
            if 'Anexo_I_Rol_2021RN' in href or 'Anexo_II_DUT_2021_RN' in href:
                print(f"Found relevant PDF: {href}")
                # Extract filename from URL
                filename = href.split('/')[-1]
                save_path = os.path.join('anexos', filename)
                if download_pdf(href, save_path):
                    pdf_files.append(save_path)
        
        # Create ZIP file with downloaded PDFs
        if pdf_files:
            create_zip(pdf_files, 'anexos/anexos.zip')
            print("\nProcess completed successfully!")
            print(f"Downloaded {len(pdf_files)} files:")
            for pdf in pdf_files:
                print(f"- {pdf}")
        else:
            print("\nNo PDF files were found or downloaded.")
            print("Please check if the website structure has changed or if the PDFs are still available.")
            
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()