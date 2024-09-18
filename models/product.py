from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db.setup import Base

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    store_id = Column(Integer, ForeignKey('stores.id'))

    # Relationship to Store
    store = relationship('Store', back_populates='products')
    
    # Relationship to Audits
    audits = relationship('Audit', back_populates='product')

    def __repr__(self):
        return f"<Product(name={self.name}, price={self.price})>"

    # Static CRUD methods
    @staticmethod
    def create(session, name, price, store_id):
        product = Product(name=name, price=price, store_id=store_id)
        session.add(product)
        session.commit()
        return product

    @staticmethod
    def get_all(session):
        return session.query(Product).all()

    @staticmethod
    def find_by_id(session, product_id):
        return session.query(Product).filter_by(id=product_id).first()

    @staticmethod
    def delete(session, product_id):
        product = session.query(Product).filter_by(id=product_id).first()
        if product:
            session.delete(product)
            session.commit()

    # Property method for validating price
    @property
    def valid_price(self):
        if self.price < 0:
            raise ValueError("Price cannot be negative!")
        return self.price
