# Megasena
>Mega-Sena game API. The user chooses how many numbers per game, and the API randomly generates the numbers. The user can also check the latest draw result and compare it with their own numbers to see how many hits they got.
<br>
# Step 1
    Create a database.

# Step 2
    This process is intended for Linux.

    Open the terminal, navigate to the cloned folder, and run:

      python3 -m venv venv
      source venv/bin/activate

# Step 3
    Run this command in the project folder:

    pip install -r requirements.txt

# Step 4
    1-In the cloned folder there is a file:
     .env.example 
     rename it to: 
     .env
    2-This file contains the database configuration line. The original setup uses PostgreSQL, so update it with your own settings:
    SQLALCHEMY_DATABASE_URI="postgresql://usuario:senha@localhost/bancodedados"


# Step 5
    To run the bot, this project uses Selenium for Python with the Firefox driver:

    1-Download the Firefox driver:
        https://github.com/mozilla/geckodriver/releases
    2-Extract the downloaded file.

    3-In the terminal, navigate to the extracted folder.

    4-Now run this command:

    sudo cp geckodriver /usr/local/bin/

    5-Selenium documentation:
        https://selenium-python.readthedocs.io/installation.html

# Step 6
    To create the tables in the database created in Step 1, run:
    first command:
    flask db stamp head
    second command:
    flask db migrate -m "inicio"
    third command:
    flask db upgrade

# Step 7
    For API requests, here is the Postman link:
    https://www.postman.com/science-pilot-55116957/workspace/testetecnicopython/request/15389359-f0641211-8d83-4758-a731-aa67751b01ee

# Step 8
    Now that everything is configured, you can run the project.
