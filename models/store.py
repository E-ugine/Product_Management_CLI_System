from sqlalchemy import Column, Integer, String
from db.setup import Base

class Store(Base):
    __tablename__ = 'stores'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    location = Column(String)

    def __repr__(self):
        return f"<Store(name={self.name}, location={self.location})>"
