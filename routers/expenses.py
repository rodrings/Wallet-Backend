from fastapi import APIRouter, HTTPException
from models import Expense, ExpenseCreate, Transaccion, TransaccionType
import data
from datetime import datetime

router = APIRouter()

@router.post("/expense")
def expense(expense : ExpenseCreate):
    if data.balanceW < expense.amount:
        raise HTTPException(status_code= 400, detail= "Not enough money")
    data.balanceW -= expense.amount
    new_transaccion = Transaccion(id = len(data.history)+1, 
                                  type = TransaccionType.Expense, 
                                  amount = expense.amount, 
                                  description= expense.description, 
                                  date= datetime.now())
    data.history.append(new_transaccion)
    return {
        "status" : "success",
        "message" : "Expense recorded",
        "balance" : data.balanceW
    }
