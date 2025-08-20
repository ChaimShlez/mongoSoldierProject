# from services.app import insert_soldier
from services.entity.soldier import Soldier
from services.dal.queries import Queries





class SoldierLogic:
    def __init__(self):
       self.queries=Queries()



    def create_soldier(self,soldier_data):
        soldier = Soldier(soldier_data.soldierID,soldier_data.
           firstName,soldier_data.lastName,soldier_data.phoneNumber,soldier_data.rank)

        return self.insert_soldier_to_data(soldier)

    def insert_soldier_to_data(self,soldier):
        if  self.queries.is_exist(soldier._soldier_id):
            return "soldier is exist"

        else:
            soldier = {"soldierID": soldier._soldier_id, "firstName": soldier._firstName, "lastName": soldier._lastName,
                       "phoneNumber": soldier._phoneNumber, "rank": soldier._rank}
            self.queries.insert(soldier)
            return "The insertion was successful."





    def get_soldiers(self):
         return self.queries.get_all()


    def delete_solider(self,soldier_id):
        result = self.queries.delete(soldier_id)

        if result.deleted_count==1:
            return "The deletion was successful."
        else:
            return "soldier do'nt exist"


    def update_solider(self, soldier_id,soldier):
        soldier_dict = soldier.dict()
        result=self.queries.update(soldier_id, soldier_dict)
        if result.matched_count==1:
            return "The update was successful."
        else:
            return "soldier do'nt exist"









