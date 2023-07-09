import sqlite3

class Registration:
    def __init__(self ):
        self.connection = sqlite3.connect("main.db")#Connect to the main database
        self.cursor = self.connection.cursor()
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS Registration (
            RegistrationId INTEGER PRIMARY KEY AUTOINCREMENT,
            MatricNo TEXT,
            SemesterId TEXT,
            CourseCodes TEXT,
            FOREIGN KEY (MatricNo) REFERENCES Students (MatricNo),
            FOREIGN KEY (SemesterId) REFERENCES Semester (SemesterId)
            )
            """
        )
    def fetch_registration_courses(self):
        self.matricNo = input("Enter student matric-no: ")
        self.semester = input("Enter semester ID: ")
        self.cursor.execute(
            f"""
            SELECT Level, YOA FROM STUDENTS WHERE MatricNo = '{self.matricNo}'
            """
        )
        result = self.cursor.fetchall()
        self.level = result[0][0]
        self.yoa = result[0][1]
        print(self.level, self.yoa)
        self.cursor.execute(
            f"""
            SELECT Semester, Session FROM SEMESTER WHERE SemesterId = '{self.semester}'
            """
        )
        result2 = self.cursor.fetchall()
        self.current_semester = result2[0][0]
        self.current_session = result2[0][1]
        print(self.current_semester, self.current_session)

        current_session_integer = int((self.current_session.split('/'))[0])
        print(current_session_integer)

        student_current_level = ((current_session_integer - self.yoa) * 100) + self.level
        print(student_current_level)


# Instance testing
regista = Registration()
regista.fetch_registration_courses()