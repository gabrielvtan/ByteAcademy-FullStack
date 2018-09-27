import os
import time

import view
from model import Database

school_database = 'school2.db'

while True:
    with Database(school_database) as db:
        os.system('clear')
        print('\nWhat woud you like to add to our DB?')
        choice = input('\n\n[C]lass\n[T]eacher\n[S]tudent\n[L]ookup\n[E]xit\n')
        
        if choice.upper() == 'C':
            view.add_class()
            class_id_ = input('Class ID: ')
            teacher_id_ = input('Teacher ID: ')
            student_id_ = input('Student ID: ')
            success = db.add_entry_class(class_id_, teacher_id_, student_id_)
            if success:
                view.success('class')
            else:
                view.error()

        elif choice.upper() == 'T':
            view.add_teacher()
            teacher_id_ = input('Teacher ID: ')
            first_ = input('First Name: ')
            last_ = input('Last Name: ')
            project_ = input('Project: ')
            success = db.add_entry_teacher(teacher_id_, first_, last_, project_)   
            if success:
                view.success('teacher')
            else:
                view.error()         
        
        elif choice.upper() == 'S':
            view.add_student()
            student_id_ = input('Student ID: ')
            first_ = input('First Name: ')
            last_ = input('Last Name: ')
            city_ = input('City: ')
            success = db.add_entry_student(student_id_, first_, last_, city_)
            if success:
                view.success('student')
            else:
                view.error()
        
        elif choice.upper() == 'L':
            lookup_choice = view.lookup()
            if lookup_choice == 'S':
                result = db.lookup_all('student')
                view.print_database(result)
            elif lookup_choice == 'C':
                result = db.lookup_all('class')
                view.print_database(result)
            elif lookup_choice == 'T':
                result = db.lookup_all('teacher')
                view.print_database(result)
            else:
                print('Error, please choose C, T, S.')
                time.sleep(2)
        
        
        elif choice.upper() == 'E':
            view.exit()
            break

        else:
            print('Invalid choice. Please type C, T, or S')
            time.sleep(3)