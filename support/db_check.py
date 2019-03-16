import mysql.connector

import credentials_var as cred


# cursor = cred.coll.find({})
# for document in cursor:
#     print(document)

# Create database if not exists
def sql_checkCreate():
    # MySQL for checking database existence
    sqlDbCheck = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd=""
    )
    sqlDbCheck.cursor().execute("CREATE DATABASE IF NOT EXISTS %s", cred.sql_db_name)


# Check if table already exists
# def table_create(dbname, tablename):
#     mydb = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         passwd="",
#         database=dbname
#     )
#
#     tableCursor = mydb.cursor()
#
#     tableNotExist = True
#     for x in tableCursor:
#         if x == tablename:
#             tableNotExist = False
#         else:
#             tableNotExist = True
#
#     if tableNotExist == True:
#         try:
#             tableCursor.execute("CREATE TABLE " + tablename + " (name VARCHAR(255), address VARCHAR(255))")
#         except:
#             print("Error creating table")
#         else:
#             print("Table created")


sql_checkCreate()
