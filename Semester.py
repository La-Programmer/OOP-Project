import sqlite3

class Semester:
    def __init__(self):
        self.connection = sqlite3.connect("main.db")#Connect to the main database
        self.cursor = self.connection.cursor()
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS Semester (
            SemesterId INTEGER PRIMARY KEY AUTOINCREMENT,
            Semester INTEGER,
            Session TEXT
            )
            """
        )
    
    def add_semester(self):
        self.semester = int(input("Enter semester: "))
        self.session = input("Enter session: ")
        self.cursor.execute(
            f"""
            INSERT INTO Semester (Semester, Session)
            VALUES ('{self.semester}', '{self.session}')
            """
        )

        self.connection.commit()
        print("Semester has successfully been added to the database")
    
    def rm_semester(self):
        id = int(input("Enter semester ID to remove: "))
        self.cursor.execute(
            f"""
            DELETE FROM Semester WHERE SemesterId = '{id}'
            """
        )
        
        self.connection.commit()
        print("Semester has successfully been deleted from the database")

semester = Semester()
semester.add_semester()

