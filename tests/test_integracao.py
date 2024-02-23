import pandas as pd
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

def test_read_data_and_check_schema():
    df = pd.read_sql('SELECT * FROM vendas', con=DATABASE_URL)

    assert not df.empty, "O DF está vazio."

    expected_dtype = {
        'id':'int64',
        'email':'object',
        'data':'datetime64[ns]',
        'valor':'float64',
        'quantidade':'int64',
        'produto':'object',
        'categoria':'object'
    }

    assert df.dtypes.to_dict() == expected_dtype, "O schema do DF não corresponde ao esperado."

