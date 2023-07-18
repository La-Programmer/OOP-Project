import sqlite3

class Results:
    def __init__(self, level):
        self.level = level
        self.connection = sqlite3.connect("main.db")
        self.cursor = self.connection.cursor()

        self.cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS Results_{self.level}L(
                MATRIC_NO TEXT PRIMARY KEY,
                {', '.join([f'{course} TEXT' for course in self.get_semester_courses()])}
            )""")

    def get_semester_courses(self):
        if self.level == 100:
            return ['MTH102', 'PHY106', 'GNE104', 'PHY102', 'CHM102', 'MTH104', 'GST102', 'GNE102', 'PHY104', 'CHM104', 'GNE106', 'GST114']
        elif self.level == 200:
            return []
        elif self.level == 300:
            return []
        elif self.level == 400:
            return []
        elif self.level == 500:
            return []

    def get_registered_students(self):
        semesterCourseList = self.get_semester_courses()
        studentsList = []

        self.cursor.execute("""
        SELECT * FROM Students
        WHERE Level = 100 AND YOA = 2020 
        """)
        results2 = self.cursor.fetchall()

        print(results2)

        # self.cursor.execute("SELECT MatricNo, CourseCodes FROM REGISTRATION")
        # results = self.cursor.fetchall()

        for result in results2:
            matricNo = result[0]
            print(matricNo)
            self.cursor.execute(f"""
            SELECT * FROM Registration
            WHERE MatricNo = '{matricNo}'
            """)

            results3 = self.cursor.fetchall()
            print(results3)

            for result in results3:
                studentCourseList = result[3].split(',')
                print(studentCourseList)
            # print('Course list to be offered during the specified semester:')
            # print(studentCourseList)
            # print('Student matriculation number:')
            # print(studentMatricNo)
            # print(semesterCourseList)

                registered_courses = []
                for i in semesterCourseList:
                    if i in studentCourseList:
                        registered_courses.append(i)

                if registered_courses:
                    studentsList.append(matricNo)
                    self.cursor.execute(
                        f"""INSERT INTO Results_{self.level}L(MATRIC_NO)
                        VALUES (?)""", (matricNo)
                    )
                    self.connection.commit()

        print(studentsList)

results1 = Results(100)
results1.get_registered_students()
