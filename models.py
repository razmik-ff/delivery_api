from uuid import uuid4
from sqlalchemy import INTEGER, VARCHAR, TEXT, Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from database import Base

class CompanyType:
    MARKET = "Market"
    RESTAURANT = "Restaurant"
    PHARMACY = "Pharmacy"
    FLOWERS = "Flowers"


class Company(Base):

    __tablename__ = "companies"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column(VARCHAR(50), nullable=False)
    type = Column(VARCHAR(20), nullable=False)
    address = Column(VARCHAR(200), nullable=False)
    tel = Column(VARCHAR(25), nullable=False)
    logo = Column(VARCHAR(255), nullable=True)

    products = relationship("Product", back_populates="company")


class Product(Base):

    __tablename__ = "products"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column(VARCHAR(50), nullable=False)
    price = Column(INTEGER, nullable=False)
    quantity = Column(INTEGER, nullable=False)
    image = Column(VARCHAR(255), nullable=True)
    description = Column(TEXT, nullable=True)
    company_id = Column(UUID(as_uuid=True), ForeignKey("companies.id"))

    company = relationship("Company", back_populates="products")

class Order(Base):

    __tablename__ = "orders"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    address = Column(VARCHAR(200), nullable=False)
    status = Column(VARCHAR(20), nullable=False)


class Basket(Base):

    __tablename__ = "baskets" 

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    product_id = Column(UUID(as_uuid=True), ForeignKey("products.id"))
    order_id = Column(UUID(as_uuid=True), ForeignKey("orders.id"))
    quantity = Column(INTEGER, nullable=False)
