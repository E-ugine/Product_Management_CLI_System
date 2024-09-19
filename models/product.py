from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db.setup import Base
from sqlalchemy.exc import IntegrityError

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)  # names must be unique to avoid duplicates
    price = Column(Integer, nullable=False)
    quantity = Column(Integer) 
    store_id = Column(Integer, ForeignKey('stores.id'))

    store = relationship('Store', back_populates='products')
    audits = relationship('Audit', back_populates='product')

    def __repr__(self):
        return f"<Product(name={self.name}, price={self.price}, quantity={self.quantity})>"

    
    @staticmethod
    def create(session, name, price, store_id, quantity=1): #this method allows create functionality
        try:          
            existing_product = session.query(Product).filter_by(name=name).first() # To avoid duplicates,check if the product already exists
            if existing_product:             
                existing_product.quantity += quantity  #  if the product exists , we add its  quantity by the number of products added
                session.commit()
                return existing_product
            else:     #if the product does not exist then we can create a new product and persist to the database      
                product = Product(name=name, price=price, store_id=store_id, quantity=quantity)
                session.add(product)
                session.commit()
                return product
        except IntegrityError: # looks at any integrity error violations. for instance 
            session.rollback()
            raise ValueError("A product with this name already exists.")

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

    @property #ensures that price is valid by only accepting positive inputs for prices
    def valid_price(self):
        if self.price < 0:
            raise ValueError("Price cannot be negative!")
        return self.price
