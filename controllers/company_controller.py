# Import the connect.py file from the database folder
from database import connect

# Define a function to store a company receiving a companyId
def show(companyId):
  # Define the query to get a company by id
  query = "SELECT * FROM companies WHERE id = %s"
  # Define the value to get a company by id
  values = (companyId,)
  # Execute the query
  connect.cursor.execute(query, values)
  # Fetch the company result
  result = connect.cursor.fetchone()
  # Return the result
  return result

# Define a function to update a company receiving a company object
def update(company):
  # Define the query to update a company
  sql = "UPDATE companies SET name = %s, address = %s WHERE id = %s"
  # Define the values to update a company
  val = (company['name'], company['address'], company['id'])
  # Execute the query
  connect.cursor.execute(sql, val)
  # Commit the changes
  connect.db.commit()
  # Print the message so the user knows the company has been updated
  print('Company information updated!')