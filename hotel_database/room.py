import datetime
from database_connection import Database


class Room:
    def __init__(self,room_id,room_type,price,available):
        self.room_id = room_id
        self.room_type = room_type
        self.price = price
        self.available = available
 

    def select_all_room():
        db = Database()
        db.connect()
        query = f"select * from Room"
        rows = db.execute_query(query)
        context = {}
        room_id_booking = ""
        count = 1
        for row in rows :
            key = f"{row[0]}"
            dict_value = {
                'Room ID' : row[0],
                'Room Type' : row[1],
                'Price' : row[2],
                'Available' : row[3],
            }
            context[key] = dict_value
            # room_id_booking = dict_value['Room ID']
            count = count +1
        return context
    
    def select_type_room(type):
        db = Database()
        db.connect()
        query = f"select * from Room where room_type ='{type}'"
        print(query)
        rows = db.execute_query(query)
        context = {}
        count = 1
        for row in rows :
            key = f"{row[0]}"
            dict_value = {
                'Room ID' : row[0],
                'Room Type' : row[1],
                'Price' : row[2],
                'Available' : row[3],
            }
            context[key] = dict_value
            # room_id_booking = dict_value['Room ID']
            count = count +1
        return context
    
    def change_price_room(type,price):
        db = Database()
        db.connect()
        query = f"UPDATE Room SET price ={price} WHERE room_type='{type}'"
        db.excute_update_query(query)

    def add(self):
        db = Database()
        db.connect()
        query ="insert into Room (room_id, room_type,price,available)\
                VALUES (?, ?, ?,?)"
        paramenters = (self.room_id, self.room_type ,self.price , self.available )
        db.execute_query_with_paramenters(query,paramenters)

    def get_price(type):
        price = 0
        db = Database()
        db.connect()
        query =f"select price from Room where room_type = '{type}'"
        rows = db.execute_query(query)
        for row in rows :
            price = row[0]
            return price
        return None



R = Room.get_price("A")
# print(R)


       
        
# t = datetime.datetime.now()
# s = str(t.strftime("%d")) + str(t.strftime("%m")) + str(t.strftime("%Y"))
# print(s)



