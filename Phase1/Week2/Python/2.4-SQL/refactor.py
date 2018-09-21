from data_access_object import Database

# 'with' means runs the enter method and exit method 
with Database('themas.db') as db:
    #db.create_table('students')
    db.add_column('students','surname')

