# Import the cursor from connect.py
from connect import cursor

# Create the database
def create_database():
  # Create the database if doesnt exist
  cursor.execute('CREATE DATABASE IF NOT EXISTS db_salarysuggestor')
  # Use the database
  cursor.execute('USE db_salarysuggestor')