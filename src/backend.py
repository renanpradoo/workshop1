import pandas as pd
from contrato import Vendas
import os
from dotenv import load_dotenv

load_dotenv(".env")

# Lê as variáveis do ambiente
POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_HOST = os.getenv('POSTGRES_HOST')
POSTGRES_PORT = os.getenv('POSTGRES_PORT')
POSTGRES_DB = os.getenv('POSTGRES_DB')

# Cria a URL de conexao com o banco de dados
DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}"

def process_excel(uploaded_file):
    try:
        df = pd.read_excel(uploaded_file)
        erros = []
        extra_cols = set(df.columns) - set(Vendas.model_fields.keys())

        if extra_cols:
            return False, f"Colunas extras detectadas no Excel: {', '.join(extra_cols)}"
        
        for index, row in df.iterrows():
            try:
                _ = Vendas(**row.to_dict())
            except Exception as e:
                erros.append(f"Erro na linha {index +2}: {e}")

        # Retorna o resultado da validacao, os erros e o df
        return df, True, erros
    
    except ValueError as ve:
        return df, False, str(ve)
    except Exception as e:
        # Se houver excecao, retorna o erro e um df vazio
        return df, False, f"Erro inesperado: {str(e)}"
    
def excel_to_sql(df):
    df.to_sql('vendas', con=DATABASE_URL, if_exists='replace', index=False)
