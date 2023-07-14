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
    
    def register_lecturer(self, id, name, yoe, uname, password):
        self.id = id
        self.name = name
        self.yoe = yoe
        self.uname = uname
        self.password = password
        self.cursor.execute(
            f"""
            INSERT INTO Lecturers
            VALUES ('{self.id}', '{self.name}', {self.yoe}, '{self.uname}', '{self.password}')
            """
        )

        self.connection.commit()
        print(self.name + " has been successfully registered")
    
    def verify_lecturer(self, uname, pwd):
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
lecturer.verify_lecturer()

