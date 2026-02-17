from database import engine, SessionLocal, Base
from models import Transaction
from datetime import date

Base.metadata.create_all(bind=engine)

db = SessionLocal()

sample_data = [
    Transaction(date=date(2025,1,1), category="groceries", amount=54.23),
    Transaction(date=date(2025,1,2), category="rent", amount=1200),
    Transaction(date=date(2025,1,3), category="entertainment", amount=20),
    Transaction(date=date(2025,2,5), category="groceries", amount=75),
]

db.add_all(sample_data)
db.commit()
db.close()

print("Database seeded!")
