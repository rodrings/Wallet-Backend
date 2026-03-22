from fastapi import FastAPI, HTTPException
from routers import wallet, expenses, investments, history

app = FastAPI()

app.include_router(wallet.router)
app.include_router(expenses.router)
app.include_router(investments.router)
app.include_router(history.router)


@app.get("/")
def root():
    return {"message": "Finance Wallet API"}









