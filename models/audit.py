from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from db.setup import Base

class Audit(Base):
    __tablename__ = 'audits'

#Table columns consist of;
    id = Column(Integer, primary_key=True) #This is the table's primary key
    product_id = Column(Integer, ForeignKey('products.id')) #the foreign key links this audit table to product table
    product_name = Column(String, nullable=False)
    audit_date = Column(Date())

    product = relationship('Product', back_populates='audits')  # defines relationship with product model. back_populates defines the two-way relationship

    def __repr__(self): #this gives a presentation of the audit model
        return f"<Audit(product_name={self.product_name}, audit_date={self.audit_date})>"
    
    #this static method provides a create functinality to create a new audit record and persist it to the database
    @staticmethod
    def create(session, product_id, product_name, audit_date):
        audit = Audit(product_id=product_id, product_name=product_name, audit_date=audit_date)
        session.add(audit)
        session.commit()
        return audit

    @staticmethod
    def get_all(session):
        return session.query(Audit).all() #retrieves all records of audit in the database

    @staticmethod
    def find_by_id(session, audit_id):
        return session.query(Audit).filter_by(id=audit_id).first()

    @staticmethod
    def delete(session, audit_id):
        audit = session.query(Audit).filter_by(id=audit_id).first()
        if audit:
            session.delete(audit)
            session.commit()
