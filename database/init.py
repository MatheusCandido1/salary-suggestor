"""
* Author: Matheus Carvalho, Amber Upton, Fatima Gonzales, Javier Segura, Sweastik Pokhrel
* Date: 12-06-2022
"""
# Import the cursor from connect.py
from connect import cursor

# Create the database
def use_database():
  # Use the database
  cursor.execute('USE db_salarysuggestor')
  # Set the foreign key check to 0
  cursor.execute('SET FOREIGN_KEY_CHECKS = 0')
  # Drop the tables if they exists
  cursor.execute('drop table if exists companies')
  cursor.execute('drop table if exists candidates')
  cursor.execute('drop table if exists proposals')
  # Set the foreign key check to 1
  cursor.execute('SET FOREIGN_KEY_CHECKS = 1')