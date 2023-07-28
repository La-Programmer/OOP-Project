import sqlite3
import pandas as pd

class Results:
    def __init__(self, level, semester, session):
        self.level = level
        self.semester = semester
        self.session = int((session.split('/'))[0])
        self.connection = sqlite3.connect("main.db")
        self.cursor = self.connection.cursor()

        if ((self.session - 2018 + 1) * 100) == level:
            self.curr = 'o'
        else:
            self.curr = 'n'

        self.cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {self.curr}Results_{self.level}L{self.semester}(
                MATRIC_NO TEXT PRIMARY KEY,
                {', '.join([f'{course} TEXT' for course in self.get_semester_courses()])},
                FOREIGN KEY (MATRIC_NO) REFERENCES Students (MatricNo)
            )""")
        
    def get_courses(self, semester, level):
        if semester == 1:
            specific_semester = "First"
        else:
            specific_semester = "Second"
        
        self.cursor.execute(
            f"""
            SELECT * FROM {self.curr}_Courses
            WHERE CourseSemester = '{specific_semester}' AND CourseLevel = {level}
            """
        )
        results = self.cursor.fetchall()
        return results

    def get_semester_courses(self):
        detailed_list = self.get_courses(self.semester, self.level)
        course_list = []
        for i in range(len(detailed_list)):
            course_list.append(detailed_list[i][0])
        
        return (course_list)

    def get_registered_students(self):
        semesterCourseList = self.get_semester_courses()
        studentsList = []

        self.cursor.execute(f"""
        SELECT * FROM Students
        WHERE level = {self.level} and YOA = 2020  
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
                    
                print(registered_courses)

                if registered_courses:
                    print(matricNo)
                    studentsList.append(matricNo)
                    self.cursor.execute(
                        f"""INSERT OR IGNORE INTO {self.curr}Results_{self.level}L{self.semester} (MATRIC_NO)
                        VALUES ('{matricNo}')"""
                    )
                    self.connection.commit()

        print(studentsList)
    


    def extract_data_and_insert(self):
        # Read data from the Excel sheet using pandas
        df = pd.read_excel("result_data.xlsx")  # Replace 'your_excel_file.xlsx' with your actual file name

        # Replace 'your_table' with the name of your table
        df.to_sql(f'{self.curr}Results_{self.level}L{self.semester}', self.connection, if_exists='replace', index=False)

        # Commit the changes and close the connection
        self.connection.commit()


results1 = Results(100, 2, '2020/2021')
results2= Results(400, 2, '2021/2022')
results1.extract_data_and_insert()