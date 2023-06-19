import sqlite3

class Lecturer:
    def __init__(self):
        self.connection = sqlite3.connect('main.db')
        self.cursor = self.connection.cursor()
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS Lecturers(
                ID INTEGER PRIMARY KEY,
                Name TEXT,
                YOE YEAR,
                Username TEXT,
                Password TEXT
            )
            """
        )
    
    def register_lecturer(self):
        self.id = input("Enter lecturer ID: ")
        self.name = input("Enter lecturer Name: ")
        self.yoe = input("Enter year of employment: ")
        self.uname = input("Enter desired username: ")
        self.password = input("Enter desired password: ")
        self.cursor.execute(
            f"""
            INSERT INTO Lecturers
            VALUES ('{self.id}', '{self.name}', {self.yoe}, '{self.uname}', '{self.password}')
            """
        )

        self.connection.commit()
        print(self.name + " has been successfully registered")
    
    def verify_lecturer(self):
        uname = input("Enter Username: ")
        pwd = input("Enter Password: ")
        self.cursor.execute(
            f"""
            SELECT NAME FROM Lecturers WHERE Username = '{uname}' AND Password = '{pwd}'
            """
        )
        results = self.cursor.fetchall()
        if not results:
            print("Wrong username or password")
        else:
            print("Welcome " + results[0][0])

    def delete_lecturer(self, id):
        self.cursor.execute(
            """
            DELETE FROM Lecturers WHERE ID = '"""+ id +"""'
            """
        )
        self.connection.commit()
        print("Lecturer with ID number "+ id +" has successfully been deleted from the system")
    
    def fectch_lecturers(self):
        self.cursor.execute(
            """
            SELECT * FROM Lecturers
            """
        )
        results = self.cursor.fetchall()
        print(results)

# EXAMPLE SCENARIO
lecturer = Lecturer()
# lecturer.register_lecturer()
lecturer.fectch_lecturers()

