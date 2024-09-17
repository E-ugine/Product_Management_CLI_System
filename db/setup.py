from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create the database engine
SQLALCHEMY_DATABASE_URL = "sqlite:///./product-management-system.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create a configured "SessionLocal" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create the Base class from which all ORM models will inherit
Base = declarative_base()
