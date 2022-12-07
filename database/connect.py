"""
* Author: Matheus Carvalho, Amber Upton, Fatima Gonzales, Javier Segura, Sweastik Pokhrel
* Date: 12-06-2022
"""
# Import mysql.connector
import mysql.connector

# Connect to the database using the credentials
db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="dbsecret",
  database="db_salarysuggestor"
)

# Create a cursor
cursor = db.cursor()