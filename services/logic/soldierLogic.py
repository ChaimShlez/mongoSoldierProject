# from services.app import insert_soldier
from services.entity.soldier import Soldier
from services.dal.queries import Queries





class SoldierLogic:
    def __init__(self):
       self.queries=Queries()



    def create_soldier(self,soldier_data):
        soldier = Soldier(soldier_data.soldierId,soldier_data.
           firstName,soldier_data.lastName,soldier_data.phoneNumber,soldier_data.rank)

        self.insert_soldier_to_data(soldier)

    def insert_soldier_to_data(self,soldier):

       soldier= {"soldierID":soldier._soldier_id,"firstName":soldier._firstName,"lastName":soldier._lastName,
                 "phoneNumber":soldier._phoneNumber,"rank":soldier._rank}
       self.queries.insert(soldier)



    def get_soldiers(self):
         return self.queries.get_all()


    def delete_solider(self,soldier_id):

        if self.queries.is_exist(soldier_id):
            self.queries.delete(soldier_id)
        else:
            return "soldier do'nt exist"

    def update_solider(self, soldier_id,soldier):

        if self.queries.is_exist(soldier_id):
            soldier_dict = soldier.dict()
            self.queries.update(soldier_id, soldier_dict)
        else:
            return "soldier do'nt exist"




