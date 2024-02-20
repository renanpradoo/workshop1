import streamlit as st

class ExcelValidatorUI:
    
    def __init__(self):
        self.set_page_config()

    def set_page_config(self):
        st.set_page_config(
            page_title="Validador de schema excel"
        )

    def display_header(self):
        st.title("Mudei esse trem")

    def upload_file(self):
        return st.file_uploader("Carregue vosso arquivo Excel aqui", type=["xlsx"])
    
    def display_results(self, result, errors):
        if errors:
            for error in errors:
                st.error(f"Erro na validação: {error}")
        else:
            st.success("O schema do arquivo Excel está correto.")