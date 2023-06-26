import sqlite3

class Courses:
    def __init__(self):
        self.connection = sqlite3.connect("main.db")#Connect to the main database
        self.cursor = self.connection.cursor()
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS Courses (
            CourseCode TEXT PRIMARY KEY,
            CourseName TEXT,
            CourseLevel INTEGER,
            CourseSemester TEXT,
            CourseCurriculum TEXT,
            Outstanding TEXT DEFAULT NULL
            )
            """
        )
    def insert_course(self):
        self.code = input("Insert course code: ")
        self.name = input("Insert course name: ")
        self.level = input("Insert course level: ")
        self.semester = input("Insert course semester: ")
        self.curriculum = input("Insert course curriculum: ")
        self.cursor.execute(
            f"""
            INSERT INTO Courses
            VALUES ('{self.code}', '{self.name}', {self.level}, '{self.semester}', '{self.curriculum}', NULL)
            """
        )

        self.connection.commit()
        print(self.name + " has been successfully added to the course list")

    def insert_many_courses(self):
        courses_data = []
        amount = int(input("How many courses would you like to insert into the databse: "))
        for i in range(amount):
            self.code = input("Insert course code: ")
            self.name = input("Insert course name: ")
            self.level = input("Insert course level: ")
            self.semester = input("Insert course semester: ")
            self.curriculum = input("Insert course curriculum: ")
            course = (self.code, self.name, self.level, self.semester, self.curriculum)
            courses_data.append(course)
        query = """
        INSERT INTO Courses (CourseCode, CourseName, CourseLevel, CourseSemester, CourseCurriculum, Outstanding)
        VALUES (?, ?, ?, ?, ?, NULL)
        """

        self.cursor.executemany(query, courses_data)
        self.connection.commit()
        print("Courses have successfully been added to the database")

    def delete_course(self):
        code = input("Insert the course code of the course you would like to delete: ")
        self.cursor.execute(
            f"""
            DELETE FROM Courses WHERE CourseCode = '{code}'
            """
        )
        self.connection.commit()
        print(code + " has successfully been deleted")

    def fetch_courses(self):
        self.cursor.execute(
            """
            SELECT * FROM Courses
            """
        )
        results = self.cursor.fetchall()
        print(results)
courses = Courses()
courses.fetch_courses()