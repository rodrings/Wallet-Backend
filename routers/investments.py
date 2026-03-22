from fastapi import APIRouter, HTTPException
from models import InvestmentCreate, Investment, Transaccion, TransaccionType
import data
from datetime import datetime

router = APIRouter()

@router.post("investment/invest")
def invest(investment : InvestmentCreate):
    if data.balanceW < investment.amount:
        raise HTTPException(status_code= 400, detail= "Not enough balance")
    data.balanceW -= investment.amount
    data.invested += investment.amount
    new_investment = Investment(amount= investment.amount, rate= investment.rate,id= len(data.investmentsL) + 1, start= datetime.now())
    data.investmentsL.append(new_investment)
    new_transaccion = Transaccion(id = len(data.history)+1, 
                                  type = TransaccionType.Investment, 
                                  amount = investment.amount, 
                                  description= f"Investment rate{investment.rate}%", 
                                  date= datetime.now())
    data.history.append(new_transaccion)
    return {
        "status" : "success",
        "message" : "Investment Created",
        "Total invested" : data.invested,
        "investments" : data.investmentsL,
        "balance" : data.balanceW
    }


@router.post("/investment/close/{id}")
def close_investment(id: int):
    

    investment = next((inv for inv in data.investmentsL if inv.id == id), None)
    

    if not investment:
        raise HTTPException(status_code=404, detail="Inversión no encontrada")
    
    ahora = datetime.now()
    tiempo = (ahora - investment.start).total_seconds() / 86400
    interes = investment.amount * (investment.rate / 100) * tiempo
    montoTotal = interes + investment.amount

    data.balanceW += montoTotal

    data.invested -= investment.amount 


    new_transaccion = Transaccion(
        id=len(data.history) + 1,
        type=TransaccionType.Investment,
        amount=montoTotal,
        description=f"Liquidate Inv. #{investment.id} | Earned: {round(interes, 4)}",
        date=ahora 
    )
    data.history.append(new_transaccion)


    data.investmentsL.remove(investment)

    return {"message": "Inversión liquidada", "monto_recibido": round(montoTotal, 2)}