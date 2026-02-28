# Financial Data Analysis API

A RESTful backend service for managing and analyzing structured financial transaction data.
Built to support reliable data processing, validation, and reporting using a relational database.

## Overview

This project implements a backend API that stores, processes, and retrieves financial transaction records. It demonstrates backend architecture, relational data modeling, and data integrity handling for applications that require consistent and accurate data processing.

The system supports transaction storage, filtering, aggregation, and validation to ensure correct and reliable handling of financial records.

## Features

- RESTful API for transaction management
- Relational database schema using MySQL
- Data validation and integrity enforcement
- Transaction filtering and aggregation queries
- Modular backend architecture
- Structured request and response handling

## Technologies Used

- Python
- FastAPI
- MySQL
- SQLAlchemy
- RESTful API design
- JSON / HTTP
- Git

## Example API Endpoints

### Add Transaction  
POST /transactions  

Request body:

{
  "amount": 50.00,
  "category": "Groceries",
  "date": "2025-01-10"
}

### Get All Transactions  
GET /transactions  

### Get Transactions by Category  
GET /transactions?category=Groceries  

### Get Summary Statistics  
GET /transactions/summary  

Returns aggregated totals and metrics.

## Data Integrity Handling

The API includes validation logic to ensure:

- Required fields are present
- Numeric values are valid
- Dates are properly formatted
- Records remain consistent across operations

This is important for applications processing financial data.

## How to Run Locally

Clone the repository:

git clone https://github.com/brushton-dev/financial-data-analysis-api.git  
cd financial-data-analysis-api  

Install dependencies:

pip install -r requirements.txt  

Start the server:

python main.py  

Access locally at:  
http://localhost:8000  

## What I Learned

- Designing RESTful backend services
- Structuring modular backend architecture
- Working with relational data models
- Writing SQL queries for aggregation and filtering
- Enforcing data validation and consistency
- Testing API behavior and handling edge cases

## Future Improvements

- Authentication and authorization
- Docker containerization
- Cloud deployment
- Automated testing
- Performance optimization for larger datasets

## Author

Brandon Rushton  
Computer Science Student, Western University
