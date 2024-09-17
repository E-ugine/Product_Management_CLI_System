from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db.setup import Base

class Store(Base):
    __tablename__ = 'stores'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    location = Column(String)

    # One store can have many products
    products = relationship('Product', back_populates='store')

    def __repr__(self):
        return f"<Store(name={self.name}, location={self.location})>"
