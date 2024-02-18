# workshop1-ao-vivo

    1. Clone o repositório:
        `` bash
        git clone https://git@github.com:renanpradoo/workshop1.git
        cd workshop1

    2. Configure a versão correta do Python no pyenv:
        ``bash 
        pyenv install 3.11.5
        pyenv local 3.11.5

    3. Instale as dependências do projeto:
        ``bash
        python -m venv .venv
        
        3.1 Linux/Mac:
            source .venv/bin/activate

        3.2 Windows:
            source .venv/Scripts/Activate

        pip install -r requirements.txt