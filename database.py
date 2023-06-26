from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

POSTGRES_DB_URL = "postgresql+psycopg2://user_delivery:pwd_delivery@localhost/delivery"

engine = create_engine(POSTGRES_DB_URL)
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)
