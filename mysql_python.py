#import libraries

import mysql.connector
from mysql.connector import Error

#create server connection

def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(host = host_name,user = user_name, passwd = user_password)
        print("mysql database connection successfull")
    except Error as err:
        print(err)
    return connection
pw = "Secure@1990"
db ="mysql_python"
connection = create_server_connection("localhost", "root", pw)

#create mysql python database


        
def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("database create successfully")
    except Error as err:
        print(err)
create_database_query = "create database mysql_python"
create_database(connection, create_database_query)

#connect to database

def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(host = host_name,user = user_name,passwd = user_password,database = db_name)
        print("mysql database connection successfull")
    except Error as err:
        print(err)
    return connection

#Execute sql queries

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("query was successfull")
    except Error as err:
        print(err)


create_consumers_table = """
create table consumers(
consumer_id int primary key,
customer_name varchar(25) not null,
product_name varchar(25) not null,
quantity int,
unit_price float);"""

#connect to the database

connection = create_db_connection("localhost","root",pw,db)
execute_query(connection, create_consumers_table)

#insert data

data_consumers = """
insert into consumers values
(101, "naveen", "laptop", 5, 50000),
(102, "praveen", "tv", 6, 60000),
(103, "shivaji", "speakers", 7, 30000),
(104, "anudeep", "phone", 7, 25000);
"""
connection = create_db_connection("localhost","root",pw,db)
execute_query(connection, data_consumers)

def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(err)
        
#using select statement
        
q1 = """
select * from consumers
"""
connection = create_db_connection("localhost","root",pw,db)
results = read_query(connection, q1)
for result in results:
    print(result)

#print some columns in table
    
q2 = """
select customer_name, product_name from  consumers;
"""
connection = create_db_connection("localhost","root",pw,db)
results = read_query(connection, q2)
for result in results:
    print(result)
    
#using distinct
    
q3 = """
select distinct product_name from  consumers;
"""
connection = create_db_connection("localhost","root",pw,db)
results = read_query(connection, q3)
for result in results:
    print(result)
    
#using where clause

q4 = """
select * from  consumers where product_name = "laptop";
"""
connection = create_db_connection("localhost","root",pw,db)
results = read_query(connection, q4)
for result in results:
    print(result)

#using order by clause
    
q5 = """
select * from  consumers order by unit_price;
"""
connection = create_db_connection("localhost","root",pw,db)
results = read_query(connection, q5)
for result in results:
    print(result)



#update command

update = """
update consumers
set customer_name = "chatrapathi"
where consumer_id = 103
"""
connection = create_db_connection("localhost","root",pw,db)
execute_query(connection, update)


q6 = """
select * from consumers where consumer_id = 103;
"""
connection = create_db_connection("localhost","root",pw,db)
results = read_query(connection, q6)
for result in results:
    print(result)

#delete command

delete_order = """
delete from consumers where consumer_id = 103;
"""
connection = create_db_connection("localhost","root",pw,db)
execute_query(connection, delete_order)

q7 = """
select * from consumers
"""
connection = create_db_connection("localhost","root",pw,db)
results = read_query(connection, q7)
for result in results:
    print(result)




    


