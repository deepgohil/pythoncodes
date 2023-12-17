# # Create Database
import mysql.connector as mc
mydb = mc.connect(
    host = "localhost",
    user = "root",
    password = "dr$Mac123#"
)

mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")
for x in mycursor:
    print(x)
# mydb = mysql.connector.connect(
#     host = "localhost",
#     user = "root",
#     password = "jyanjain252003"
# )

# mycursor = mydb.cursor()

# mycursor.execute("create database furniture")

# # Check database
# import mysql.connector

# mydb = mysql.connector.connect(
#     host = "localhost",
#     user = "root",
#     password = "jyanjain252003"
# )

# mycursor = mydb.cursor()

# mycursor.execute("show databases")
# for x in mycursor:
#     print(x)

# Create Table

# import mysql.connector

# mydb = mysql.connector.connect(
#     host = "localhost",
#     user = "root",
#     password = "jyanjain252003",
#     database = "furniture"
# )

# mycursor = mydb.cursor()

# mycursor.execute("""create table cupboard(
#     id int(15) not null,
#     name varchar(75) not null,
#     price float not null,
#     count int not null,
#     primary key(id)
# )
# """
# )

# mycursor.execute("show tables")
# for x in mycursor:
#     print(x)

# mycursor.execute("""insert into cupboard(id,name,price,count)
#                  values(6,"cb31",7500,8)
# """)
# mydb.commit()

# sql = ("""insert into cupboard(id,name,price,count) values(%s,%s,%s,%s)""")
# val = [
#     (2, 'cb2', 15000, 5),
#     (3, 'cb3', 7000, 15),
#     (4, 'cb4', 20000, 3),
#     (5, 'cb5', 40000, 5)   
# ]

# mycursor.executemany(sql,val)
# mydb.commit()

# mycursor.execute("delete from cupboard where name='cb31'")
# mydb.commit()

# mycursor.execute("select * from cupboard")
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)

