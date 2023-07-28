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

    def register_student(self, matricNo, name, level, yoa, dept, uname, password):
        self.matricNo = matricNo
        self.name = name
        self.level = level
        self.yoa = yoa
        self.dept = dept
        self.uname = uname
        self.password = password
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

    def student_verify(self, uname, pwd):
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
student.register_student('EU210303-2879', 'Kaseem Bello', 100, 2020, 'Computer Engineering', 'kaseem.bello', '1234567890')