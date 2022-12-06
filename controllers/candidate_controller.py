# Import the connect.py file from the database folder
from database import connect

# Define a function to store a candidate receiving a candidate object
def store(candidate):
  # Define the query to insert a candidate
  query = "INSERT INTO candidates (name, address, email, phone, experience_level, employment_type) VALUES (%s, %s, %s, %s, %s, %s)"
  # Define the values to insert a candidate
  values = tuple(candidate.values())
  # Execute the query
  connect.cursor.execute(query, values)
  # Commit the changes
  connect.db.commit()
  # Print the message so the user knows the candidate has been created
  print('Candidate created successfully.')

# Define a function to get all candidates
def index():
  # Define the query to get all candidates
  connect.cursor.execute("SELECT * FROM candidates")
  # Fetch all the candidates
  result = connect.cursor.fetchall()
  # Return the result
  return result

# Define a function to get a candidate by id receiving a candidateId
def show(candidateId):
  # Define the query to get a candidate by id
  query = 'SELECT * FROM candidates WHERE id = %s'
  # Define the value to get a candidate by id
  value = (candidateId,)
  # Execute the query
  connect.cursor.execute(query, value)
  # Fetch the candidate result
  result = connect.cursor.fetchone()
  # Check if the result is None
  if result == None:
    # Return False is result is None
    return False 
  else:
    # Return the result
    return result
# Define a function to update a candidate receiving a candidate object
def update(candidate):
  # Define the query to update a candidate
  query = 'UPDATE candidates SET name = %s, address = %s, email = %s, phone = %s, experience_level = %s, employment_type = %s WHERE id = %s'
  # Define the values to update a candidate
  attrs = list(candidate.values())
  # Save the candidateId
  candidateId = attrs[0]
  # Remove the candidateId from the list
  attrs.pop(0)
  # Append the candidateId to the end of the list
  attrs.append(candidateId)
  # Convert the list to a tuple
  values = tuple(attrs,)
  # Execute the query
  connect.cursor.execute(query, values)
  # Commit the changes
  connect.db.commit()
  # Print the message so the user knows the candidate has been updated
  print('Candidate updated successfully.')

# Define a function to delete a candidate receiving a candidateId
def delete(candidateId):
  # Define the query to delete a candidate
  query = 'DELETE FROM candidates WHERE id = %s'
  # Define the value to delete a candidate
  value = (candidateId,)
  # Execute the query
  connect.cursor.execute(query, value)
  # Commit the changes
  connect.db.commit()
  # Print the message so the user knows the candidate has been deleted
  print('Candidate has been deleted.')