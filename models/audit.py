from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db.setup import Base  # Import Base from your setup file

class Audit(Base):
    __tablename__ = 'audits'

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey('products.id'))
    product_name = Column(String, nullable=False)
    audit_date = Column(String)
    
    # Relationship to fetch the product for an audit
    product = relationship('Product', back_populates='audits')

    def __repr__(self):
        return f"<Audit(product_name={self.product_name}, audit_date={self.audit_date})>"
