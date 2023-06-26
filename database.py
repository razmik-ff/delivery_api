from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg2://user_delivery:pwd_delivery@localhost/delivery"
)
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)
