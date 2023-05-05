import os
from dotenv import load_dotenv

# carregar as variáveis de ambiente do arquivo .env.test
load_dotenv(".env.test")

# definir as variáveis do ambiente de teste
os.environ["TESTING"] = "True"
os.environ["DATABASE_URL"] = os.getenv("TEST_DATABASE_URL")

# importar as dependências necessárias
from microservice.app.database import engine
from microservice.app.models import Base


# definir o código a ser executado antes dos testes
def setup_module(module):
    Base.metadata.create_all(bind=engine)


# definir o código a ser executado após os testes
def teardown_module(module):
    Base.metadata.drop_all(bind=engine)
