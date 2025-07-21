import os
from dotenv import load_dotenv

load_dotenv()

db_user = os.environ.get('DB_USER')
db_password = os.environ.get('DB_PASSWORD')
db_host = os.environ.get('DB_HOST')
db_port = os.environ.get('DB_PORT')
db_name = os.environ.get('DB_DATABASE')

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'uma-chave-secreta-dificil-de-adivinhar'
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or 'outra-chave-jwt-muito-secreta'
    
    SQLALCHEMY_DATABASE_URI = f'mysql+mysqlconnector://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False