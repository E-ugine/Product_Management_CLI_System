from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db.setup import Base

class Store(Base):
    __tablename__ = 'stores'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    location = Column(String)

    # One-to-many relationship with Product
    products = relationship('Product', back_populates='store')

    def __repr__(self):
        return f"<Store(name={self.name}, location={self.location})>"

    # Static CRUD methods
    @staticmethod
    def create(session, name, location):
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
    def delete(session, store_id):
        store = session.query(Store).filter_by(id=store_id).first()
        if store:
            session.delete(store)
            session.commit()
