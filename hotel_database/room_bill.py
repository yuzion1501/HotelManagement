import datetime
from database_connection import Database


class Bill:
    def __init__(self,id,charge,addition,foreigner_addition,compensation,total):
        self.id = id
        self.charge = charge
        self.addition = addition
        self.foreigner_addition = foreigner_addition
        self.compensation = compensation
        self.total = total        
    def calculate(self):
       print(self.total)

    def context(self):
        dict = {
            'id' : self.id,
            'charge' : self.charge,
            'addition' : self.addition,
            'foreigner_addition' : self.foreigner_addition,
            'total' : self.total,
        }
        return dict
    
    def add(self):
        db = Database()
        db.connect()
        query ="insert into Bill (id, charge,addition,foreigner_addition,compensation,total)\
                VALUES (?, ?, ?,?, ?, ?)"
        paramenters = (self.id,self.charge,self.addition,self.foreigner_addition,0,self.total)
        db.execute_query_with_paramenters(query,paramenters)

       
        
# t = datetime.datetime.now()
# s = str(t.strftime("%d")) + str(t.strftime("%m")) + str(t.strftime("%Y"))
# print(s)



