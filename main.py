import psycopg2
from task_db import hostname, database, username, pwd, port_id


try:
    cnnct =psycopg2.connect(
                host = hostname,
                dbname = database,
                user = username,
                password = pwd,
                port = port_id
            )
    
    cnnct.autocommit = True
    cur = cnnct.cursor()

# Created room table 
    create_room = ''' CREATE TABLE IF NOT EXISTS room (
                            room_id  SERIAL PRIMARY KEY,       
                            room_number int)'''
    
    cur.execute(create_room)

# Insering data to the table room
    insert_script1  = 'INSERT INTO room (room_id, room_number) VALUES (%s, %s)'
    insert_data1 = [(1, 5), (2, 3), (3, 8)]
    for record2 in insert_data1:
        cur.execute(insert_script1, record2)
    print("[INFO] Data to the table ROOM was succefully inserted")

# Update data in the table person
    update_room = 'UPDATE room SET room_number = 12 WHERE room_id = 1;'
    cur.execute(update_room)
    print("[INFO] Table ROOM was succefully updated")

# Get data from the table room
    cur.execute("SELECT room_number FROM room WHERE room_id = 1;")
    print(cur.fetchone())
    print("[INFO] Table from ROOM was succefully resived")

# # Deleting the table room
    # cur.execute('DROP TABLE IF EXISTS room;')
    # print("[INFO] Table ROOM was deleted")

# Created person table  
    create_person = ''' CREATE TABLE IF NOT EXISTS person (
                            id  SERIAL PRIMARY KEY,
                            full_name varchar(40) NOT NULL,
                            mail varchar(40) NOT NULL,
                            phone int NOT NULL,
                            room_id int NOT NULL REFERENCES room (room_id),
                            created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP)'''
    cur.execute(create_person)

# Inserted data to the table person
    insert_script  = 'INSERT INTO person (id, full_name, mail, phone,room_id) VALUES (%s, %s, %s, %s, %s)'
    insert_data = [(1, 'James Doe', 'smthing1@gmail.com', 1234567, 1), (2, 'Robin Djain', 'smthing2@gmail.com', 9876543, 2), (3, 'Xavier Faza', 'smthing3@gmail.com', 1234598, 3)]
    for record in insert_data:
        cur.execute(insert_script, record)
    print("[INFO] Data to the table PERSON was succefully inserted")

# Update data in the table person
    update_person = 'UPDATE person SET phone = 9999999 WHERE id = 1;'
    cur.execute(update_person)
    print("[INFO] Table PERSON was succefully updated")
    

# Get data from the table person
    cur.execute("SELECT mail FROM person WHERE full_name = 'James Doe';")
    print(cur.fetchone())
    print("[INFO] Table from PERSON was succefully resived")

# Deleting the table room
    # cur.execute('DROP TABLE IF EXISTS room;')
    # print("[INFO] Table PERSON was deleted")

# Create table timestamp
    TimeStamp = (''' CREATE TABLE IF NOT EXISTS time_stamp(
                        id  SERIAL PRIMARY KEY,
                        ts TIMESTAMP,
                        current_time 
                    )''')

    # cnnct.commit()

except Exception as error:
    print("[INFO] Error while working with PostgreSQL", error)
finally:
    if cnnct is not None:
        cnnct.close()
        print("[INFO] PostgreSQL connection closed")
