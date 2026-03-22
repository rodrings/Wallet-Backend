from fastapi import APIRouter
from models import  Transaccion, TransaccionType
import data
from typing import List, Optional

router = APIRouter()

@router.get("/history")
# Agregamos el "= None" al final
def history(type: Optional[TransaccionType] = None): 
    if type: 
        # Filtramos y devolvemos la lista (sin f-string para que sea JSON)
        filtered = [t for t in data.history if t.type == type]
        return filtered[::-1]
    
    # Devolvemos la lista completa invertida (sin f-string)
    return data.history[::-1]