import sqlite3

class Student:
    def __init__(self):
        self.connection = sqlite3.connect('main.db') #Connect to main database file
        self.cursor = self.connection.cursor()
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS Students (
                MatricNo TEXT PRIMARY KEY,
                Name TEXT,
                Level INT,
                YOA YEAR,
                Dept TEXT,
                Uname TEXT,
                Password TEXT
            )
            """
        )

    def register_student(self):
        self.matricNo = input("Enter student matriculation number: ")
        self.name = input("Enter student name: ")
        self.level = input("Enter student level: ")
        self.yoa = input("Enter student year of admission: ")
        self.dept = "Computer Engineering"
        self.uname = input("Enter desired username: ")
        self.password = input("Enter desired password: ")
        self.cursor.execute(
            f"""
            INSERT INTO Students
            VALUES ('{self.matricNo}', '{self.name}', {self.level}, {self.yoa}, '{self.dept}', '{self.uname}', '{self.password}')
            """
        )

        self.connection.commit()
        print(self.matricNo + " has been successfully registered")
    
    def retrieve_student(self, matricNo):
        self.cursor.execute(
            """
            SELECT * FROM Students
            WHERE MatricNo = '"""+ matricNo +"""'
            """
        )
        results = self.cursor.fetchall()
        print(results)

    def delete_student(self, matricNo):
        self.cursor.execute(
            """
            DELETE FROM Students WHERE MatricNo = '"""+ matricNo +"""'
            """
        )
        self.connection.commit()
        print("Student with matriculation number "+ matricNo +" has successfully been deleted from the system")

    def student_verify(self):
        uname = input("Enter username: ")
        pwd = input("Enter password: ")
        self.cursor.execute(
            f"""
            SELECT Name FROM Students WHERE Uname = '{uname}' AND Password = '{pwd}'
            """
        )
        results = self.cursor.fetchall()
        if not results:
            print("Wrong username or password")
        else:
            print("Welcome " + results[0][0])
    
    def fetch_students(self):
        self.cursor.execute(
            """
            SELECT * FROM Students
            """
        )
        results = self.cursor.fetchall()
        print(results)
    
# EXAMPLE
student = Student()
student.student_verify()