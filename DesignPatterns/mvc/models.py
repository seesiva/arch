import json

class Car(object):

    def __init__(self, car_name = None, car_model = None):
        self.car_name = car_name
        self.car_model = car_model
    #returns Person name, ex: John Doe
    def name(self):
        return ("%s %s" % (self.car_name,self.car_model))

    @classmethod
    #returns all people inside db.txt as list of Person objects
    def getAll(self):
        database = open("D:\\MV\\arch\\mvc\\db.txt", "r")
        result = []
        json_list = json.loads(database.read())
        for item in json_list:
            item = json.loads(item)
            car = Car(item['car_name'], item['car_model'])
            result.append(car)
        return result
    