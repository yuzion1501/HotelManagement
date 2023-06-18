import datetime
from database_connection import Database



def get_data_roomA():
        db = Database()
        db.connect()

        query ="select COUNT(room_id) from Reservation where room_id like 'A%' and status = 'accept'"
        rows = db.execute_query(query)
        num_of_bookings= rows[0][0]

        query2 = "select duration from Reservation where room_id like 'A%' and status = 'accept'"
        rows = db.execute_query(query2)
        sum = 0
        for row in rows:
            sum = sum + row[0]

        query3 = "select total from Reservation R Right join Bill B on R.id = B.id\
                    where R.status = 'accept' and R.room_id like 'A%'"
        rows = db.execute_query(query3)
        revenue = 0
        for row in rows:
            revenue = revenue + row[0]

        return num_of_bookings,sum,revenue
    
def get_data_roomB():
        db = Database()
        db.connect()

        query ="select COUNT(room_id) from Reservation where room_id like 'B%' and status = 'accept'"
        rows = db.execute_query(query)
        num_of_bookings= rows[0][0]

        query2 = "select duration from Reservation where room_id like 'B%' and status = 'accept'"
        rows = db.execute_query(query2)
        sum = 0
        for row in rows:
            sum = sum + row[0]

        query3 = "select total from Reservation R Right join Bill B on R.id = B.id\
                    where R.status = 'accept' and R.room_id like 'B%'"
        rows = db.execute_query(query3)
        revenue = 0
        for row in rows:
            revenue = revenue + row[0]

        return num_of_bookings,sum,revenue
    
def get_data_roomC():
        db = Database()
        db.connect()

        query ="select COUNT(room_id) from Reservation where room_id like 'C%' and status = 'accept'"
        rows = db.execute_query(query)
        num_of_bookings= rows[0][0]

        query2 = "select duration from Reservation where room_id like 'C%' and status = 'accept'"
        rows = db.execute_query(query2)
        sum = 0
        for row in rows:
            sum = sum + row[0]

        query3 = "select total from Reservation R Right join Bill B on R.id = B.id\
                    where R.status = 'accept' and R.room_id like 'C%'"
        rows = db.execute_query(query3)
        revenue = 0
        for row in rows:
            revenue = revenue + row[0]

        return num_of_bookings,sum,revenue
    

def get_data_report():
        pA1,pA2,pA3 = get_data_roomA()
        pB1,pB2,pB3 = get_data_roomB()
        pC1,pC2,pC3 = get_data_roomC()

        dict = {
            'total bookings of room A' : pA1,
            'total booking days of room A' : pA2,
            "revenue of room A" : pA3,

            'total bookings of room B' : pB1,
            'total booking days of room B' : pB2,
            "revenue of room B" : pB3,

            'total bookings of room C' : pC1,
            'total booking days of room C' : pC2,
            "revenue of room C" : pC3
        }
        return dict
    
    



       
        
# t = datetime.datetime.now()
# s = str(t.strftime("%d")) + str(t.strftime("%m")) + str(t.strftime("%Y"))
# print(s)



