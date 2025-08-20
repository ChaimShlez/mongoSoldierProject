from fastapi import FastAPI
from pydantic import BaseModel
from typing_extensions import reveal_type

from .logic.soldierLogic import SoldierLogic

app=FastAPI()
soldier_logic = SoldierLogic()

class SoldierData(BaseModel):
    soldierID: int
    firstName: str
    lastName: str
    phoneNumber:str
    rank: str

@app.post("/addSoldier")
def insert_soldier(data: SoldierData):
    print("Received data:", data)
    try:
        return soldier_logic.create_soldier(data)
    except Exception as e:
        return {"dont success", "error",e}


@app.get("/getSoldiers")
def get_soldiers():
    try:
       return soldier_logic.get_soldiers()
    except Exception as e:
       return {"dont success", "error", e}


@app.put('/putSoldier/{soldier_id}')
def update_soldier(soldier_id: int, data: SoldierData):
    try:
        return soldier_logic.update_solider(soldier_id,data)
    except Exception as e:
       return {"dont success", "error", e}





@app.delete('/deleteSoldier/{soldier_id}')
def delete_soldier(soldier_id:int):
    try:
        return soldier_logic.delete_solider(soldier_id)
    except Exception as e:
       return {"dont success", "error", e}

