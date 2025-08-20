from services.dal.ConnectionWrapper import ConnectionWrapper


class Queries:
    def __init__(self):
        self._connection=ConnectionWrapper()




    def get_all(self,collection_name="soldiers"):
        return list(self._connection.get_collection(collection_name).find({},{"_id":0}))

    def insert(self, soldier_data,collection_name="soldiers"):
        return self._connection.get_collection(collection_name).insert_one(soldier_data)

    def update(self, soldier_id, update_data,collection_name="soldiers"):
        result= self._connection.get_collection(collection_name).update_one({"soldierID": soldier_id}, {"$set": update_data})
        return result

    def delete(self, soldier_id,collection_name="soldiers"):
       result =self._connection.get_collection(collection_name).delete_one({"soldierID": soldier_id})

       return result

    def is_exist(self,soldier_id ,collection_name="soldiers"):
        return self._connection.get_collection(collection_name).find_one({"soldierID":soldier_id},{"_id":0})

