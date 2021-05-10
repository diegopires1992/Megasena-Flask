# Megasena
>API de jogos da mega sena, o usuario deverá escolher a quantidade de dezenas por jogo e sua API irá gerar aleatoriamente dezenas para o usuário. O usuário poderá consultar o resultado do ultimo jogo e comparar com suas dezenas para conferir quantos numeros acertou..
<br>
# Passo1
    faça a criação de uma base de dados.

# Passo2
    Este processo é destinado para linux

    Abra o terminal e navegue ate a pasta clonada e rode o comando:

      python3 -m venv venv
      source venv/bin/activate

# Passo3
    Execute no terminal na pasta onde esta o projeto:

    pip install -r requirements.txt

# Passo4
    1-Na pasta clonada tem um arquivo:
     .env.example 
     renomeie o mesmo para: 
     .env
    2-Nesse arquivo tem a linha para configuração do banco e o  banco utilizado foi o postgresql agora altere para suas configurações:
    SQLALCHEMY_DATABASE_URI="postgresql://usuario:senha@localhost/bancodedados"


# Passo5
    Para executar o robo estou usando a biblioteca selenium para python com driver para firefox:

    1-Baixe o arquivo do driver firefox:
        https://github.com/mozilla/geckodriver/releases
    2-Faça a extração do mesmo.

    3-Navegue pelo terminal ate a pasta extraida do arquivo 

    4-Agora que esta na pasta certa faça o comando no terminal:

    sudo cp geckodriver /usr/local/bin/

    5-Link documentação selenium:
        https://selenium-python.readthedocs.io/installation.html

# Passo6
    Para criar as tabelas no banco que já foi criado no passo1 vamos usar o comando:
    primeiro comando:
    flask db stamp head
    segundo comando:
    flask db migrate -m "inicio"
    teceiro comando:
    flask db upgrade

# Passo7
    Para as requisição da API aqui esta link do postman:
    https://www.postman.com/science-pilot-55116957/workspace/testetecnicopython/request/15389359-f0641211-8d83-4758-a731-aa67751b01ee

# Passo8
    Agora que esta tudo configurado podemos rodar o projeto.
