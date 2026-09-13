from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Text 
from sqlalchemy.orm import sessionmaker, declarative_base


# CONFIGURACOES DO SYSTEMA
engine = create_engine("sqlite:///cadastro.db")
Base = declarative_base()
Session = sessionmaker(bind=engine)

# CRIAR AS TABELAS
class Cliente(Base):
    __tablename__ = "clientes"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(40), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    hash = Column(Text, nullable=False)


Base.metadata.create_all(engine)
