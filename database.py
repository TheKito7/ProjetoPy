from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

#DATABASE_URL = "mysql+pymysql://root:root@localhost:3307/bdpessoas02"
# Modelo da estrutura:
# "mysql+pymysql://USUARIO:SENHA@localhost:3306/bdpessoas02"

DATABASE_URL = "mysql+pymysql://root:@localhost:3307/bdpessoas02"



engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit = False,
    autoflush=False,
    bind = engine    
)

Base = declarative_base()
