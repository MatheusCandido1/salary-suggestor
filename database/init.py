# Import the cursor from connect.py
from connect import cursor

# Create the database
def use_database():
  # Use the database
  cursor.execute('USE db_salarysuggestor')