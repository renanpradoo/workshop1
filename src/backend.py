import pandas as pd
from contrato import Vendas

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
        # return df, True, erros
        return True, erros
    
    except Exception as e:
        # Se houver excecao, retorna o erro e um df vazio
        return pd.DataFrame(), f"Erro inesperado: {str(e)}"
