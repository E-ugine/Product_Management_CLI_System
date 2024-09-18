from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db.setup import Base
from sqlalchemy.exc import IntegrityError

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True)  # Ensuring unique names for merging
    price = Column(Integer, nullable=False)
    quantity = Column(Integer, default=1)  # New quantity field to track product count
    store_id = Column(Integer, ForeignKey('stores.id'))

    store = relationship('Store', back_populates='products')
    audits = relationship('Audit', back_populates='product')

    def __repr__(self):
        return f"<Product(name={self.name}, price={self.price}, quantity={self.quantity})>"

    # Static method to create or update the quantity of a product
    @staticmethod
    def create(session, name, price, store_id, quantity=1):
        try:
            # Check if the product already exists
            existing_product = session.query(Product).filter_by(name=name).first()

            if existing_product:
                # Update the quantity of the existing product
                existing_product.quantity += quantity
                session.commit()
                return existing_product
            else:
                # Create a new product
                product = Product(name=name, price=price, store_id=store_id, quantity=quantity)
                session.add(product)
                session.commit()
                return product
        except IntegrityError:
            session.rollback()
            raise ValueError("A product with this name already exists or another integrity constraint violated.")

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

    @property
    def valid_price(self):
        if self.price < 0:
            raise ValueError("Price cannot be negative!")
        return self.price
