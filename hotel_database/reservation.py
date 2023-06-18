import datetime
from database_connection import Database
from room_bill import Bill
from room import Room



class Booking_Form:
    def __init__(self,id,phone,	room_id,status,booking_date,date_sent,duration,number_of_guests,foreigner):
        self.id =id
        self.phone =phone
        self.room_id =room_id
        self.status =status
        self.booking_date =booking_date
        self.date_sent =date_sent
        self.duration =duration
        self.number_of_guests =number_of_guests
        self.foreigner =foreigner
    
    def change_status(self,status):
        self.status =status


    def add(self):
        db = Database()
        db.connect()
        query ="insert into Reservation (id, phone,room_id,status,booking_date,date_sent,duration,number_of_guests,foreigner)\
                VALUES (?, ?, ?,?, ?, ?,?, ?, ?)"
        paramenters = (self.id,self.phone ,self.room_id ,self.status ,self.booking_date ,self.date_sent ,self.duration ,self.number_of_guests \
                       ,self.foreigner )
        db.execute_query_with_paramenters(query,paramenters)

    def delete(id):
        db = Database()
        db.connect()
        query =f"delete from Reservation where id ='{id}'"
        db.excute_delete_query(query)
    
    def get (id):
        db = Database()
        db.connect()
        query =f"select * from Reservation where id ='{id}'"
        rows = db.execute_query(query)
        dict_value = None
        for row in rows :
            dict_value = {
            'id' : row[0],
            'phone' : row[1],
            'room_id' : row[2],
            'status' : row[3],
            'booking_date' : row[4],
            'date_sent' : row[5],
            'duration' : row[6],
            'number_of_guests' : row[7],
            'foreigner' : row[8],
            }
        return Booking_Form (dict_value['id'],dict_value['phone'],dict_value['room_id'],dict_value['status'],dict_value['booking_date'],dict_value['date_sent'],dict_value['duration'],dict_value['number_of_guests'],dict_value['foreigner'])

    def invoice(self):
        id  = self.id
        charge  = Room.get_price(id[0])* self.duration
        # if id[0] == "A":
        #     charge  = 150000 * self.duration
        # elif id[0] == "B":
        #     charge  = 170000 * self.duration
        # else:
        #     charge = 200000 * self.duration
        addition = 0
        if self.number_of_guests==3:
            addition = 0.25
        foreigner_addition =0
        if self.foreigner.strip() == "Yes":
            foreigner_addition = 0.5
        total = charge*(1+addition+foreigner_addition)
        return Bill(id,charge,addition,foreigner_addition,0,total)
    





