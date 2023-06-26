from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from uuid import UUID
import crud, models, schemas
from database import SessionLocal, engine


app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def home():
    return {"message": "Hello World"}

@app.get("/companies")
def get_companies(db: Session = Depends(get_db)):
    result = crud.get_companies(db)
    return result

@app.post("/companies")
def create_company(company: schemas.CompanyCreate, db: Session = Depends(get_db)):
    result = crud.create_company(db, company)
    return result

@app.get("/companies/{company_id}", response_model=schemas.Company)
def read_user(company_id: UUID, db: Session = Depends(get_db)):
    db_company = crud.get_company(db, company_id=company_id)
    if db_company is None:
        raise HTTPException(status_code=404, detail="Company not found")
    return db_company
