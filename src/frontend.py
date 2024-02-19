import streamlit as st

class ExcelValidatorUI:
    
    def __init__(self):
        self.set_page_config()

    def set_page_config(self):
        st.set_page_config(
            page_title="Validador de schema excel"
        )

    def display_header(self):
        st.title("Validador de schema excel?")

    def upload_file(self):
        return st.file_uploader("Carregue vosso arquivo Excel aqui", type=["xlsx"])