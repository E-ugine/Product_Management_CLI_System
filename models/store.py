from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db.setup import Base

class Store(Base):
    __tablename__ = 'stores'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    location = Column(String)

    
    products = relationship('Product', back_populates='store', cascade='all, delete')

    def __repr__(self):
        return f"<Store(name={self.name}, location={self.location})>"

   
    @staticmethod
    def create(session, name, location): # this method creates a new store and persists it to the database
        store = Store(name=name, location=location)
        session.add(store)
        session.commit()
        return store

    @staticmethod
    def get_all(session):
        return session.query(Store).all()

    @staticmethod
    def find_by_id(session, store_id):
        return session.query(Store).filter_by(id=store_id).first()

    @staticmethod
    def delete(session, store_id): # this method enables deletion of a store by its ID, and cascade delete associated products
        store = session.query(Store).filter_by(id=store_id).first()
        if store:
            session.delete(store)
            session.commit()
            return True
        return False
