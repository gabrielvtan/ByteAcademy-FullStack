import os
import time
from model import Database

school_database = 'school.db'

while True:
    with Database(school_database) as db:
        os.system('clear')
        print('\n\nWhat woud you like to add to our DB?')
        choice = input('\n\n[C]lass\n[T]eacher\n[S]tudent\n[E]xit')
        if choice.upper() == 'C':
            class_id_ = input('Class ID: ')
            teacher_id_ = input('Teacher ID: ')
            student_id_ = input('Student ID: ')
            db.add_entry_class(class_id_, teacher_id_, student_id_)
        elif choice.upper() == 'T':
            teacher_id_ = input('Teacher ID: ')
            first_ = input('First Name: ')
            last_ = input('Last Name: ')
            project_ = input('Project: ')
            db.add_entry_teacher(teacher_id_, first_, last_, project_)            
        elif choice.upper() == 'S':
            student_id_ = input('Student ID: ')
            first_ = input('First Name: ')
            last_ = input('Last Name: ')
            city_ = input('City: ')
            db.add_entry_student(student_id_, first_, last_, city_)
        elif choice.upper() == 'E':
            print('\n\nExiting.....')
            break
        else:
            print('Invalid choice. Please type C, T, or S')
            time.sleep(3)