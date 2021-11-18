import db
from sqlalchemy import String, Column, Integer, Float


class Products(db.Base):
    __tablename__ = "product"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Float)

    