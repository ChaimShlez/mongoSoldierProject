from services.dal.ConnectionWrapper import ConnectionWrapper


class Queries:
    def __init__(self):
        self._connection=ConnectionWrapper()




    def get_all(self):
        return list(self._connection.get_collection().find({},{"_id":0}))

    def insert(self, soldier_data):
        return self._connection.get_collection().insert_one(soldier_data)

    def update(self, soldier_id, update_data):
        result= self._connection.get_collection().update_one({"soldierID": soldier_id}, {"$set": update_data})
        return result

    def delete(self, soldier_id):
       result =self._connection.get_collection().delete_one({"soldierID": soldier_id})

       return result

    def is_exist(self,soldier_id ):
        return self._connection.get_collection().find_one({"soldierID":soldier_id},{"_id":0})

