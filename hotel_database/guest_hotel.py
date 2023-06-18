import datetime
from database_connection import Database


class Guest:
    def __init__(self,name,email,phone,id_card):
        self.name =name
        self.email =email
        self.phone =phone
        self.id_card =id_card
    def add(self):
       db = Database()
       db.connect()
       query ="insert into Guest (name, email,phone,id_card) VALUES (?, ?, ?,?) "
       paramenters = (self.name, self.email,self.phone,self.id_card)
       db.execute_query_with_paramenters(query,paramenters)
    
    def has_register(phone):
        db = Database()
        db.connect()
        query =f"SELECT phone from Guest where phone ='{phone}'"
        rows = db.execute_query(query)
        print(rows)
        if len(rows) ==0:
            return False
        else:
            return True
        
# t = datetime.datetime.now()
# s = str(t.strftime("%d")) + str(t.strftime("%m")) + str(t.strftime("%Y"))
# print(s)



