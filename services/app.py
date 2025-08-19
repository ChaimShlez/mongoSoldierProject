from fastapi import FastAPI
from pydantic import BaseModel
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
async def insert_soldier(data: SoldierData):
    print("Received data:", data)

    soldier_logic.create_soldier(data)

    return {"status": "ok"}

@app.get("/getSoldiers")
async def get_soldiers():
   return soldier_logic.get_soldiers()

@app.put('/putSoldier/{soldier_id}')
async def update_soldier(soldier_id: int, data: SoldierData):
    soldier_logic.update_solider(soldier_id,data)
    return {"status": "ok"}




@app.delete('/deleteSoldier/{soldier_id}')
async def delete_soldier(soldier_id:int):
    return soldier_logic.delete_solider(soldier_id)

