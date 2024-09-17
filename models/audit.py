from sqlalchemy import Column, Integer, String, ForeignKey
from db.setup import Base

class Audit(Base):
    __tablename__ = 'audits'

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey('products.id'))
    product_name = Column(String, nullable=False)
    audit_date = Column(String)

    def __repr__(self):
        return f"<Audit(product_name={self.product_name}, audit_date={self.audit_date})>"
