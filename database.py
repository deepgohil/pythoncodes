# import mysql.connector
# mydb = mysql.connector.connect(
#     host = 'localhost',
#     user = 'root',
#     password = 'dr$Mac123#',
# )
# mycursor = mydb.cursor()
# mycursor.execute("create database furniture")

# import mysql.connector
# mydb = mysql.connector.connect(
#     host = 'localhost',
#     user = 'root',
#     password = 'dr$Mac123#'
# )
# mycursor = mydb.cursor()
# mycursor.execute("show databases")
# for x in mycursor:
#     print(x)

# import mysql.connector
# mydb = mysql.connector.connect(
#     host = 'localhost',
#     user = 'root',
#     password = 'dr$Mac123#',
#     database = "furniture"
# )
# mycursor = mydb.cursor()
# mycursor.execute("""create table cupboard(
#         id int(15) not null,
#         name varchar(75) not null,
#         price float not null,
#         count int not null,
#         primary key(id)
# )""")

# import mysql.connector
# mydb = mysql.connector.connect(
#     host = 'localhost',
#     user = 'root',
#     password = 'dr$Mac123#',
#     database = 'furniture'
# )
# mycursor = mydb.cursor()
# mycursor.execute("show tables")
# for x in mycursor:
#     print(x)

# import mysql.connector
# mydb = mysql.connector.connect(
#     host = 'localhost',
#     user = 'root',
#     password = 'dr$Mac123#',
#     database = 'furniture'
# )
# mycursor = mydb.cursor()
# mycursor.execute("""insert into cupboard(id, name, price, count)
# values (6, 'cb31', 7500, 8)""")
# mydb.commit()

# import mysql.connector
# mydb = mysql.connector.connect(
#     host = 'localhost',
#     user = 'root',
#     password = 'dr$Mac123#',
#     database = 'furniture'
# )
# mycursor = mydb.cursor()
# mycursor.execute("""insert into cupboard(id, name, price, count) values 
# (2, 'cb2', 15000, 5),
# (3, 'cb3', 7000, 15),
# (4, 'cb4', 20000, 3),
# (5, 'cb5', 40000, 5)""")

# mydb.commit()
# print(mycursor.rowcount, 'record(s) inserted.')

# import mysql.connector
# mydb = mysql.connector.connect(
#     host = 'localhost',
#     user = 'root',
#     password = 'dr$Mac123#',
#     database = 'furniture'
# )
# mycursor = mydb.cursor()
# mycursor.execute("delete from cupboard where name = 'cb31'")

# mydb.commit()
# print(mycursor.rowcount, 'record(s) deleted.')

import mysql.connector
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'dr$Mac123#',
    database = 'furniture'
)
mycursor = mydb.cursor()
mycursor.execute("select * from cupboard")

myresult = mycursor.fetchall()
for x in myresult:
    print(x)