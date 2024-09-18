from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db.setup import Base

class Audit(Base):
    __tablename__ = 'audits'

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey('products.id'))
    product_name = Column(String, nullable=False)
    audit_date = Column(String)

    # Relationship to Product
    product = relationship('Product', back_populates='audits')

    def __repr__(self):
        return f"<Audit(product_name={self.product_name}, audit_date={self.audit_date})>"

    # Static CRUD methods
    @staticmethod
    def create(session, product_id, product_name, audit_date):
        audit = Audit(product_id=product_id, product_name=product_name, audit_date=audit_date)
        session.add(audit)
        session.commit()
        return audit

    @staticmethod
    def get_all(session):
        return session.query(Audit).all()

    @staticmethod
    def find_by_id(session, audit_id):
        return session.query(Audit).filter_by(id=audit_id).first()

    @staticmethod
    def delete(session, audit_id):
        audit = session.query(Audit).filter_by(id=audit_id).first()
        if audit:
            session.delete(audit)
            session.commit()
