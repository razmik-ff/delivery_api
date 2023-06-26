from pydantic import BaseModel
from uuid import UUID


class CompanyBase(BaseModel):

    name: str
    type: str
    address: str
    tel: str
    logo: str = None


class CompanyCreate(CompanyBase):
    pass


class Company(CompanyCreate):

    id: UUID

    class Config:

        orm_mode = True


class ProductBase(BaseModel):

    name: str
    price: int
    quantity: int
    image: str
    description: str


class ProductCreate(ProductBase):
    pass

class Product(ProductCreate):

    id: UUID
    company_id: UUID

    class Config:

        orm_mode = True


class Order(BaseModel):

    id: UUID
    address: str
    status: str


class Basket(BaseModel):

    id: UUID
    product_id: UUID
    order_id: UUID
    quantity: int

    class Config:

        orm_mode = True
