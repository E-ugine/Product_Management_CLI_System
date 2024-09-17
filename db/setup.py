from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Initialize the SQLite database URL (database file will be created automatically)
DATABASE_URL = 'sqlite:///product_management.db'

# Create an engine, which connects to the SQLite database
engine = create_engine(DATABASE_URL)

# Base class for our models (Product, Store, Audit will inherit from this)
Base = declarative_base()

# Create a configured "Session" class for database transactions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency function to get the session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
