from fastapi import APIRouter, HTTPException
from models import Wallet, Deposit, DepositCreate, Transaccion, TransaccionType
import data
from datetime import datetime

router = APIRouter()

@router.get("/wallet")
def wallet():
    earned = 0
    invested_total = 0 
    for investment in data.investmentsL:
        invested_total += investment.amount
        dias = (datetime.now() - investment.start).total_seconds()/86400
        earned += investment.amount * (investment.rate/100) * dias
    
    return Wallet(
        balance= data.balanceW, 
        invested_capital= invested_total, 
        accrued_balance= round(earned, 4), 
        total= round(data.balanceW + invested_total + earned, 2),
        investments= data.investmentsL,
        history= (data.history[::-1])
    )


@router.post("/deposit")
def deposit(deposit: DepositCreate):
    data.balanceW += deposit.amount
    new_transaccion = Transaccion(id = len(data.history)+1, 
                                  type = TransaccionType.Deposit, 
                                  amount = deposit.amount, 
                                  description= f"Deposit from {deposit.origin}", 
                                  date= datetime.now())
    data.history.append(new_transaccion)
    return {"status": "success",
            "message": f"${deposit.amount} has been added to your balance",
            "balance": data.balanceW
            }