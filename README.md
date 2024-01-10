Database can be ( CREATE | INSERT | UPDATE | DELETE ) via Python

How to automate PostgreSql transactions via PYTHON script 

-->   Install and import the psycopg2 library 

-->   gather up credentials (hostname, username, database, password and port) from pgadmin.

-->   connect the database with psycopg2 and input the above mentioned credentals 

-->   to perform database transactions like DDL, DQL, DML etc, cursor will be required
      (Make sure close the database connection and cursor)

-->   Now transactions like CREATE, INSERT, UPDATE, DELETE can be performed without hassle.  
