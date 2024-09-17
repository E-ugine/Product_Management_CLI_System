from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db.setup import Base

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    store_id = Column(Integer, ForeignKey('stores.id'))

    store = relationship('Store', back_populates='products')

    def __repr__(self):
        return f"<Product(name={self.name}, price={self.price})>"
