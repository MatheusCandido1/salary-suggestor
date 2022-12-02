from connect import mycursor

def create_database():
  mycursor.execute('CREATE DATABASE IF NOT EXISTS db_salarysuggestor')
  mycursor.execute('USE db_salarysuggestor')