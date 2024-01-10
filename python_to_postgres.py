import psycopg2 
import psycopg2.extras

hostname ='localhost'
datbase = 'demo'
username = 'postgres'
pwd = 'password'
port_id = '5432'

conn = None
try:
    with psycopg2.connect(
                host = hostname,
                dbname = datbase,
                user = username,
                password = pwd,
                port = port_id) as conn:

        with conn.cursor(cursor_factory= psycopg2.extras.DictCursor) as cur:

            cur.execute('DROP TABLE IF EXISTS employee ')
            create_script = '''CREATE TABLE IF NOT EXISTS employee(
                                id     int PRIMARY KEY,
                                NAME   varchar(40) NOT NULL,
                                salary int,
                                dept_id varchar(30))'''
            
            cur.execute(create_script)

            insert_script = 'INSERT INTO employee (id, name,salary, dept_id) VALUES (%s, %s, %s, %s)'
            insert_value = [(1, 'James', 12000, 'D1'),(2, 'Ramos', 24000, 'D3'),(3, 'Sagi', 14000, 'D2')]
            for record in insert_value:
                cur.execute(insert_script, record)
            
            update_script = 'UPDATE employee SET salary = salary + (salary * 0.5)'
            cur.execute(update_script)

            delete_script = 'DELETE FROM employee WHERE name = %s'
            delete_record = ('James',)
            cur.execute(delete_script,delete_record)

            cur.execute('SELECT * FROM EMPLOYEE')
            for record in cur.fetchall():
                print(record['name'],record['salary'])

except Exception as error:
    print(error)
finally:
    if conn is not None:
        conn.close()