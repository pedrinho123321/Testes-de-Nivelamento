# Pedro Vilas Boas Vasconcelos
# TESTES DE NIVELAMENTO - Intuitive Care
# Teste 1 - Transformação de Dados
# linguagem usa Python

import os
import pandas as pd
import tabula
import zipfile
from PyPDF2 import PdfReader

def extract_table_from_pdf(pdf_path):
    print(f"Extracting tables from {pdf_path}")
    
    tables = tabula.read_pdf(pdf_path, pages='all', multiple_tables=True)
    
    df = pd.concat(tables, ignore_index=True)
    
    df.columns = df.columns.str.strip()
    
    return df

def replace_abbreviations(df):
    print("Replacing abbreviations in columns")
    
    od_mapping = {
        'OD': 'Segmentação Assistencial',
        'AMB': 'Ambulatorial',
        'HCO': 'Hospitalar com Obstetrícia',
        'HSO': 'Hospitalar sem Obstetrícia',
        'REF': 'Referência',
        'PAC': 'Plano Ambulatorial + Hospitalar com Obstetrícia',
        'AMB, HCO': 'Ambulatorial, Hospitalar com Obstetrícia',
        'AMB, HSO': 'Ambulatorial, Hospitalar sem Obstetrícia'
    }
    
    if 'OD' in df.columns:
        df['OD'] = df['OD'].replace(od_mapping)
    
    amb_mapping = {
        'AMB': 'Ambulatorial',
        'HOS': 'Hospitalar',
        'PAC': 'PAC (Procedimentos de Alta Complexidade)',
        'AMB/HOS': 'Ambulatorial/Hospitalar'
    }
    
    if 'AMB' in df.columns:
        df['AMB'] = df['AMB'].replace(amb_mapping)
    
    return df

def main():
    if not os.path.exists('downloads'):
        os.makedirs('downloads')
        print("Created downloads directory")
    
    pdf_path = 'downloads/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf'
    
    if not os.path.exists(pdf_path):
        print(f"Error: PDF file not found at {pdf_path}")
        print("Please run the scraper.py script first to download the PDF file.")
        return
    
    try:
        df = extract_table_from_pdf(pdf_path)
        
        df = replace_abbreviations(df)
        
        csv_path = 'downloads/rol_procedimentos.csv'
        df.to_csv(csv_path, index=False, encoding='utf-8')
        print(f"Saved data to {csv_path}")
        
        zip_path = 'downloads/Teste_(Pedro_Vasconcelos).zip'
        with zipfile.ZipFile(zip_path, 'w') as zipf:
            zipf.write(csv_path, os.path.basename(csv_path))
        print(f"Created zip file: {zip_path}")
        
        print("\nProcess completed successfully!")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
