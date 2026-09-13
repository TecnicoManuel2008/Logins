import os

class Config:

   # Chave Secreta
   SECRET_KEY = os.environ.get("SECRET_KEY")

   SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class DevConfig(Config):
   DEBUG = True

class ProdConfig(Config):
   DEBUG = False

