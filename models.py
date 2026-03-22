from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional
from enum import Enum



class DepositCreate(BaseModel):
    amount: float
    origin: str

class Deposit(DepositCreate):
    date : datetime

class ExpenseCreate(BaseModel):
    amount: float
    description: str

class Expense(ExpenseCreate):
    date: datetime

class InvestmentCreate(BaseModel):
    amount: float
    rate: float

class Investment(InvestmentCreate):
    id : int
    start : datetime

class TransaccionType(str, Enum):
    Deposit = "deposit"
    Expense = "expense"
    Investment = "investment"

class Transaccion(BaseModel):
    id:int
    type: TransaccionType
    amount: float
    description: str
    date: datetime


class Wallet(BaseModel):
    balance: float 
    invested_capital: float
    accrued_balance: float
    total: float
    investments: List[Investment]
    history :List[Transaccion]
