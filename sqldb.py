# install Mysql on the computer
# pip install mysql
# pip install mysql-connector-python
# pip install mysql-connector

import mysql.connector

data_base = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='root'
)
# prepare cursor
cursor = data_base.cursor()

cursor.execute("CREATE DATABASE gofar")

cursor.close()

print("Done")
