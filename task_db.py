import psycopg2

hostname = 'localhost'
database = 'tech_task'
username = 'postgres'
pwd = '11042000'
port_id = 5432
cnnct = None 
cor = None

try:
    cnnct =psycopg2.connect(
                host = hostname,
                dbname = database,
                user = username,
                password = pwd,
                port = port_id
            )
    
    cur = cnnct.cursor()

    # cur.execute('DROP TABLE IF EXISTS room')

    create_room = ''' CREATE TABLE IF NOT EXISTS room (
                            room_id  SERIAL PRIMARY KEY,       
                            room_number int)'''
    
    cur.execute(create_room)

    insert_script1  = 'INSERT INTO room (room_id, room_number) VALUES (%s, %s)'
    insert_data1 = [(1, 1), (2, 2), (3, 3)]
    for record2 in insert_data1:
        cur.execute(insert_script1, record2)

    cur.execute('DROP TABLE IF EXISTS person')

    create_person = ''' CREATE TABLE IF NOT EXISTS person (
                            id  SERIAL PRIMARY KEY,
                            full_name varchar(40) NOT NULL,
                            mail varchar(40) NOT NULL,
                            phone int NOT NULL,
                            room_id int NOT NULL REFERENCES room (room_id))'''
    cur.execute(create_person)

    insert_script  = 'INSERT INTO person (id, full_name, mail, phone,room_id) VALUES (%s, %s, %s, %s, %s)'
    insert_data = [(1, 'James Doe', 'smthing1@gmail.com', 1234567, 1), (2, 'Robin Djain', 'smthing2@gmail.com', 9876543, 2), (3, 'Xavier Faza', 'smthing3@gmail.com', 1234598, 3)]
    for record in insert_data:
        cur.execute(insert_script, record)

    cnnct.commit()

except Exception as error:
    print(error)
finally:
    if cnnct is not None:
        cnnct.close()
