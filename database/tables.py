# Import the cursor from connect.py
from connect import cursor

# Define a function to create the tables
def create_tables():
  # Call the functions to create the `companies` table
  create_companies_table()
  # Call the functions to create the `candidates` table
  create_candidates_table()
  # Call the functions to create the `proposals` table
  create_proposals_table()
  print('Tables created successfully')

# Define function to create the companies table
def create_companies_table():
  # Create the `companies` table if it doesn't exist
  cursor.execute("CREATE TABLE IF NOT EXISTS companies (id int(11) primary key not null auto_increment, name VARCHAR(80), address VARCHAR(100), city VARCHAR(60), color VARCHAR(7), benefits text, employees int(11))")

# Define function to create the candidates table
def create_candidates_table():
  # Create the `candidates` table if it doesn't exist
  cursor.execute("CREATE TABLE IF NOT EXISTS candidates (id int(11) primary key not null auto_increment, name VARCHAR(80), address VARCHAR(100), email VARCHAR(80), phone VARCHAR(30), experience_level VARCHAR(20), employment_type VARCHAR(2))")

# Define function to create the proposals table
def create_proposals_table():
  # Create the `proposals` table if it doesn't exist
  cursor.execute("CREATE TABLE IF NOT EXISTS proposals (id int(11) primary key not null auto_increment, candidate_id int(11), proposal_date datetime default now(), job_title VARCHAR(100), salary float(10,2), status VARCHAR(20), foreign key (candidate_id) references candidates(id) on delete cascade)")