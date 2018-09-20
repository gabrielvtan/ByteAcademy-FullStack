from data_access_object import Database

with Database('themas.db') as db:
    #db.create_table('students')
    db.add_column('students','surname')
