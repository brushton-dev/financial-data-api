from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from database import SessionLocal
from models import Transaction
from pydantic import BaseModel
from datetime import date
import pandas as pd

app = FastAPI(title="Financial Data Analysis API")

class TransactionCreate(BaseModel):
    date: date
    category: str
    amount: float


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # fine for local demo
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "API running"}

@app.get("/transactions")
def get_transactions():
    db = SessionLocal()
    data = db.query(Transaction).all()
    db.close()

    return [
        {"id": t.id, "date": str(t.date), "category": t.category, "amount": t.amount}
        for t in data
    ]

@app.get("/transactions/category/{category}")
def get_transactions_by_category(category: str):
    db = SessionLocal()
    data = db.query(Transaction).filter(Transaction.category == category).all()
    db.close()

    return [
        {"id": t.id, "date": str(t.date), "category": t.category, "amount": t.amount}
        for t in data
    ]

@app.post("/transactions")
def create_transaction(tx: TransactionCreate):
    db = SessionLocal()

    new_tx = Transaction(
        date=tx.date,
        category=tx.category,
        amount=tx.amount
    )

    db.add(new_tx)
    db.commit()
    db.refresh(new_tx)  # gets the generated id
    db.close()

    return {
        "id": new_tx.id,
        "date": str(new_tx.date),
        "category": new_tx.category,
        "amount": new_tx.amount
    }


@app.get("/summary")
def summary():
    db = SessionLocal()
    data = db.query(Transaction).all()
    db.close()

    df = pd.DataFrame([{"date": t.date, "category": t.category, "amount": t.amount} for t in data])

    if df.empty:
        return {"total_spent": 0, "average_transaction": 0, "transaction_count": 0}

    return {
        "total_spent": float(df["amount"].sum()),
        "average_transaction": float(df["amount"].mean()),
        "transaction_count": int(len(df)),
    }
