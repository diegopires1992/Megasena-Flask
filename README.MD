# Passo1:
    Este processo é destinado para linux

    Abra o terminal e navegue ate a pasta clonada e rode o comando:

      python3 -m venv env
      source env/bin/activate

# Passo2
    Execute no terminal na pasta onde esta o projeto:

    pip install requirements.txt

# Passo3
    1-Na pasta clonada tem um arquivo:
     .env.example 
     renomeie o mesmo para: 
     .env
    2-Nesse arquivo tem a linha para configuração do banco e o  banco utilizado foi o postgresql agora altere para suas configurações:
    SQLALCHEMY_DATABASE_URI="postgresql://usuario:senha@localhost/bancodedados"


# Passo4
    Para executar o robo estou usando a biblioteca selenium para python com driver para firefox:

    1-Baixe o arquivo do driver firefox:
        https://github.com/mozilla/geckodriver/releases
    2-Faça a extração do mesmo.

    3-Navegue pelo terminal ate a pasta extraida do arquivo 

    4-Agora que esta na pasta certa faça o comando no terminal:

    sudo cp geckodriver /usr/local/bin/

    5-Link documentação selenium:
        https://selenium-python.readthedocs.io/installation.html

# Passo4
    Para as requisição da API aqui esta link do postman:
    https://www.postman.com/science-pilot-55116957/workspace/testetecnicopython/request/15389359-f0641211-8d83-4758-a731-aa67751b01ee

# Passo5
    Agora que esta tudo configurado podemos rodar o projeto.
