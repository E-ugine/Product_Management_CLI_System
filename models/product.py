from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db.setup import Base  # Import Base from your setup file

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    store_id = Column(Integer, ForeignKey('stores.id'))

    # Many products can belong to one store
    store = relationship('Store', back_populates='products')

    # One product can have many audits
    audits = relationship('Audit', back_populates='product')

    def __repr__(self):
        return f"<Product(name={self.name}, price={self.price})>"
