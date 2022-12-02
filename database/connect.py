import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="db_salarysuggestor"
)

mycursor = mydb.cursor()