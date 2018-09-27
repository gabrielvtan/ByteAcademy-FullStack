import sqlite3

class Database:
    def __init__(self, database_name):
         self.connection = sqlite3.connect(database_name, check_same_thread = False)
         self.cursor = self.connection.cursor()

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        if self.connection:
            self.connection.commit()
            self.cursor.close()
            self.connection.close()
        else:
            print('Unfinished control flow in database')
            pass
    
    def add_entry_class(self, class_id_, teacher_id_, student_id_):
        self.cursor.execute(
            """INSERT INTO class(
                class_id,
                teacher_id,
                student_id
                ) VALUES (
                ?,
                ?,
                ?
                );""", (
                    '{}'.format(class_id_),
                    '{}'.format(teacher_id_),
                    '{}'.format(student_id_)
                )
            )
        return True

    def add_entry_student(self, student_id_, first_, last_, city_):
        self.cursor.execute(
            """INSERT INTO student(
                student_id,
                first,
                last,
                city
                ) VALUES (
                ?,
                ?,
                ?,
                ?
                );""", (
                    '{}'.format(student_id_),
                    '{}'.format(first_),
                    '{}'.format(last_),
                    '{}'.format(city_),
                )
            )
        return True

    def add_entry_teacher(self, teacher_id_, first_, last_, project_):
        self.cursor.execute(
            """INSERT INTO teacher(
                teacher_id,
                first,
                last,
                project
                ) VALUES (
                ?,
                ?,
                ?,
                ?
                );""", (
                    '{}'.format(teacher_id_),
                    '{}'.format(first_),
                    '{}'.format(last_),
                    '{}'.format(project_),
                )
            )
        return True
    
    def lookup_all(self, table_name):
        sql = """SELECT * FROM {};""".format(table_name)
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result