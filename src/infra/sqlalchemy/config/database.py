# Importa as classes necessárias do SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define a URL do banco de dados. Atualmente, está configurado para usar um banco de dados SQLite.
# Se desejar usar PostgreSQL, a linha comentada abaixo pode ser descomentada.
SQLALCHEMY_DATABASE_URL = "sqlite:///./app_blx.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

# Cria uma instância de motor (engine) do SQLAlchemy, que representa a conexão com o banco de dados.
# O argumento `check_same_thread=False` é utilizado quando se usa SQLite para evitar problemas de concorrência.
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Cria uma instância do SessionLocal, que é uma fábrica de sessões do SQLAlchemy.
# Essa instância será usada para interagir com o banco de dados.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Cria uma classe de base (Base) para declarar modelos (tabelas) do banco de dados.
# Essa classe é usada para criar classes de modelo que mapeiam para tabelas no banco de dados.
Base = declarative_base()


def criar_bd():
    Base.metadata.create_all(bind=engine)
    
    
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()