import pyodbc

# Connect to the SQL Server database
class Database:
    def __init__(self):
        self.conn = None
        self.cursor =None
    def connect(self):
        try:
            self.conn = pyodbc.connect(
            "Driver={SQL Server};"
            "Server=DESKTOP-O3E0EIE\SQLEXPRESS;"
            "Database=HotelManagement;"
            "uid=son;"
            "pwd=1;"
            )
            self.cursor = self.conn.cursor()

        except pyodbc.Error as e:
            print("Error connecting to SQL Server:", e)

    def execute_query(self, query):
        try:
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
            return rows
        except pyodbc.Error as e:
            print("Error executing query:", e)
            return None
        
    def execute_query_with_paramenters(self,query,p):
        try:
            #self.cursor.execute(query,paramenters)
            self.cursor.execute(query,p)
            self.cursor.commit()
            # return rows
        except pyodbc.Error as e:
            print("Error executing query:", e)
            return None
        
    def excute_delete_query(self, query):
        try:
            self.cursor.execute(query)
            self.cursor.commit()
        except pyodbc.Error as e:
            print("Error executing query:", e)
            return None
        
    def excute_update_query(self, query):
        try:
            self.cursor.execute(query)
            self.cursor.commit()
        except pyodbc.Error as e:
            print("Error executing query:", e)
            return None
