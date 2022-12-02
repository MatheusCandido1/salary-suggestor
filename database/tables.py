from connect import mycursor

def create_tables():
  create_companies_table()
  create_candidates_table()
  create_proposals_table()

# Create table Companies
def create_companies_table():
  mycursor.execute("CREATE TABLE IF NOT EXISTS companies (id int(11) primary key not null auto_increment, name VARCHAR(255), address VARCHAR(255))")

# Create table Candidates
def create_candidates_table():
  mycursor.execute("CREATE TABLE IF NOT EXISTS candidates (id int(11) primary key not null auto_increment, name VARCHAR(255), address VARCHAR(255))")

# Create table Proposals
def create_proposals_table():
  mycursor.execute("CREATE TABLE IF NOT EXISTS proposals (id int(11) primary key not null auto_increment, candidate_id int(11), salary float(10,2), foreign key (candidate_id) references candidates(id))")