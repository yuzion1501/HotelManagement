from datetime import datetime,timedelta
from database_connection import Database

def create_schedule():
    db = Database()
    db.connect()
    schedule = {}
    query = f"select booking_date,duration from Reservation where status != 'reject' "
    rows = db.execute_query(query)
    for row in rows :
        i = 0
        date = datetime.strptime(row[0], "%Y-%m-%d")
        while (i<row[1]):
            temp = date + timedelta(days=i)
            schedule[temp] = 'Has Booked'
            i = i+1
    # s = datetime.strptime("6/7/2023", "%d/%m/%Y")
    return schedule

create_schedule()


       
        
# t = datetime.datetime.now()
# s = str(t.strftime("%d")) + str(t.strftime("%m")) + str(t.strftime("%Y"))
# print(s)



