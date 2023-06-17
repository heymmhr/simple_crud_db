import sqlite3

dbase = sqlite3.connect('Our_data.db') #Open a database File
print ('Database opened')


#primaru key cannot be duplicated
dbase.execute('''CREATE TABLE IF NOT EXISTS employee_records(
    ID INT PRIMARY KEY NOT NULL,
    NAME TEXT NOT NULL,
    DIVISION TEXT NOT NULL,
    STARS INT NOT NULL)''')

print ('Table created')

def insert_record(ID,NAME,DIVISION,STARS):
    dbase.execute('''INSERT INTO employee_records (ID,NAME,DIVISION,STARS) 
        VALUES(?,?,?,?)''', (ID,NAME,DIVISION,STARS))
    
    dbase.commit()
    print('Record inserted')

# insert_record(6,'Bob','Hardware',4)
# insert_record(1,'Harry','Software',3)
# insert_record(7,'Haland','Hardware',5)
# insert_record(2,'DeBruney','Technical',5)
# insert_record(3,'Harry','Software',5)

def read_Data():
    # from math import *

    data = dbase.execute('''SELECT * FROM employee_records ORDER BY STARS desc''')
    for record in data:
        print('ID : ' + str(record[0]))
        print('NAME : ' + str(record[1]))
        print('DIVISION : ' + str(record[2]))
        print('STARS :' + str(record[3]) + '\n')
    
# read_Data()

def update_record():
    dbase.execute('''UPDATE employee_records set STARS = 3 WHERE ID = 6''')
    dbase.commit()
    print('Updated')

# update_record()

def delete_record():
    dbase.execute('''DELETE from employee_records WHERE ID = 6''')
    dbase.commit()
    print('Deleted')

delete_record()
print('-------------')
read_Data()


