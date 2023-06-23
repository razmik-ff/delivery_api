from sqlalchemy.orm import Session
from sqlalchemy.dialects.postgresql import UUID

from . import models, schemas


def get_company(db: Session, company_id: UUID):
    return db.query(models.Company).filter(models.Company.id == company_id).first()

def get_product(db: Session, product_id: UUID):
    return db.query(models.Product).filter(models.Product.id == product_id).first()

def get_companies(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Company).offset(skip).limit(limit).all()

def get_products(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Product).offset(skip).limit(limit).all()

def create_company(db: Session, company: schemas.CompanyCreate):
    db_company = models.Company(
        name=company.name,
        type=company.type,
        address=company.address,
        tel=company.tel,
        logo=company.logo,
    )
    db.add(db_company)
    db.commit()
    db.refresh(db_company)
    return db_company

def create_product(db: Session, product: schemas.ProductCreate, company_id: UUID):
    db_product = models.Company(
        **product.dict(),
        company_id=company_id
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product
