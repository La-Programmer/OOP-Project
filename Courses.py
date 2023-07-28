import sqlite3

class Courses:
    def __init__(self):
        self.connection = sqlite3.connect("main.db")#Connect to the main database
        self.cursor = self.connection.cursor()
        # self.cursor.execute(
        #     """
        #     CREATE TABLE IF NOT EXISTS o_Courses (
        #     CourseCode TEXT PRIMARY KEY,
        #     CourseName TEXT,
        #     CourseLevel INTEGER,
        #     CourseSemester TEXT,
        #     CourseCurriculum TEXT,
        #     Outstanding INTEGER DEFAULT 1,
        #     CourseUnits INTEGER DEFAULT NULL
        #     )
        #     """
        # )


        # self.cursor.execute(
        #     """
        #     SELECT * FROM Courses
        #     """
        # )

        # table_data = self.cursor.fetchall()

        # self.cursor.executemany(
        #     """
        #     INSERT INTO o_Courses (CourseCode, CourseName, CourseLevel, CourseSemester, CourseCurriculum, Outstanding, CourseUnits)
        #     VALUES (?, ?, ?, ?, ?, ?, ?)
        #     """, table_data
        # )

        # self.connection.commit()

    def insert_course(self):
        self.code = input("Insert course code: ")
        self.name = input("Insert course name: ")
        self.level = input("Insert course level: ")
        self.semester = input("Insert course semester: ")
        self.curriculum = input("Insert course curriculum: ")
        self.units = input("Insert course units: ")
        if (self.curriculum == "Old"):
            curr = "o_Courses"
        else:
            curr = "n_Courses"
        self.cursor.execute(
            f"""
            INSERT INTO {curr}
            VALUES ('{self.code}', '{self.name}', {self.level}, '{self.semester}', '{self.curriculum}', NULL, {self.units})
            """
        )

        self.connection.commit()
        print(self.name + " has been successfully added to the course list")

    def insert_many_courses(self):
        amount = int(input("How many courses would you like to insert into the databse: "))
        for i in range(amount):
            self.code = input("Insert course code: ")
            self.name = input("Insert course name: ")
            self.level = input("Insert course level: ")
            self.semester = input("Insert course semester: ")
            self.curriculum = input("Insert course curriculum: ")
            self.units = input("Input course units: ")

            if (self.curriculum == "Old"):
                curr = "o_Courses"
            else:
                curr = "n_Courses"
            query = f"""
            INSERT INTO {curr} (CourseCode, CourseName, CourseLevel, CourseSemester, CourseCurriculum, Outstanding, CourseUnits)
            VALUES ('{self.code}', '{self.name}', '{self.level}', '{self.semester}', '{self.curriculum}', NULL, {self.units})
            """
            self.cursor.execute(query)
            self.connection.commit()
            print(self.name + " has successfully been added to the database")

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

    def alter_course_units(self):
        number = int(input("Insert the number of courses you would like to alter: "))
        for i in range(number):
            code = input("Insert the course code whose units you want to alter: ")
            units = input("Insert units for the course: ")
            self.cursor.execute(
                f"""
                UPDATE n_Courses 
                SET CourseUnits = {units} 
                WHERE CourseCode = '{code}'
                """
            )
            self.connection.commit()
            print("Course units have been successfully changed")
courses = Courses()
courses.insert_course()