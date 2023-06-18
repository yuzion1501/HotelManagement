from datetime import datetime
from reservation import Booking_Form
from database_connection import Database


def manage_form(status):
    condition = ""
    if status == "pending":
        condition = "where status ='pending'"
    db = Database()
    db.connect()
    query = f"select * from Reservation {condition}"
    rows = db.execute_query(query)
    context = {}
    count = 1
    for row in rows :
        key = f"key{count}"
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
        context[key] = dict_value
        count = count +1
    return context

def manage_form_for_guest(phone):
    db = Database()
    db.connect()
    query = f"select * from Reservation where phone = '{phone}'"
    rows = db.execute_query(query)
    context = {}
    room_id_booking = ""
    count = 1
    for row in rows :
        key = f"key{count}"
        dict_value = {
            'id' : row[0],
            'phone' : row[1],
            'Room ID' : row[2],
            'Booking date' : row[4],
            'Date sent' : row[5],
            'Duration' : row[6],
            'Number of guests' : row[7],
            'Foreigner' : row[8],
            'status' : row[3]
        }
        context[key] = dict_value
        room_id_booking = dict_value['id']
        count = count +1
    return context,room_id_booking


# data = manage_form()
# for key,value in data.items():
#     print(value['id'])