from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db.setup import Base
from sqlalchemy.exc import IntegrityError

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    _price = Column(Integer, nullable=False)  # Private attribute for the setter
    store_id = Column(Integer, ForeignKey('stores.id'))

    store = relationship('Store', back_populates='products')

    def __repr__(self):
        return f"<Product(name={self.name}, price={self.price})>"

    # Getter and Setter for price with validation
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self._price = value

    # Static CRUD methods
    @staticmethod
    def create(session, name, price, store_id):
        try:
            product = Product(name=name, price=price, store_id=store_id)
            session.add(product)
            session.commit()
            return product
        except ValueError as e:
            session.rollback()  # Rollback the transaction in case of error
            raise e

    @staticmethod
    def delete(session, product_id):
        product = session.query(Product).filter_by(id=product_id).first()
        if product:
            session.delete(product)
            session.commit()

