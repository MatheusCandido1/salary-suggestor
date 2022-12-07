"""
* Author: Matheus Carvalho, Amber Upton, Fatima Gonzales, Javier Segura, Sweastik Pokhrel
* Date: 12-06-2022
"""
# Import the connect.py file from the database folder
from database import connect

# Define a function to store a proposal receiving a proposal object
def store(proposal):
  # Define the query to insert a proposal
  query = "INSERT INTO proposals (candidate_id, job_title, salary, status) VALUES (%s, %s, %s, %s)"
  # Define the values to insert a proposal
  values = tuple(proposal.values())
  # Execute the query
  connect.cursor.execute(query, values)
  # Commit the changes
  connect.db.commit()
  # Print the message so the user knows the proposal has been created
  print("Proposal created successfully.")

# Define a function to get all proposals
def index():
  # Define the query to get all proposals
  query = "SELECT proposals.id as proposal_id, candidate_id, proposal_date, job_title, salary, status, name, address, experience_level, employment_type FROM proposals INNER JOIN candidates ON proposals.candidate_id = candidates.id"
  connect.cursor.execute(query)
  # Fetch all the proposals
  result = connect.cursor.fetchall()
  # Return the result
  return result

# Define a function to get a proposal by id receiving a proposalId
def show(proposalId):
  # Define the query to get a proposal by id
  query = "SELECT proposals.id as proposal_id, candidate_id, proposal_date, job_title, salary, status, name, address, experience_level, employment_type FROM proposals INNER JOIN candidates ON proposals.candidate_id = candidates.id WHERE proposals.id = %s"
  # Define the value to get a proposal by id
  val = (proposalId,)
  # Execute the query
  connect.cursor.execute(query, val)
  # Fetch the proposal result
  result = connect.cursor.fetchone()
  # Return the result
  return result

# Define a function to update a proposal receiving a proposal object
def update(proposal):
  # Define the query to update a proposal
  query = "UPDATE proposals SET candidate_id = %s, job_title = %s, salary = %s, status = %s WHERE id = %s"
  # Define the values to update a proposal
  attrs = list(proposal.values())
  # Save the proposalId
  proposalId = attrs[0]
  # Remove the proposalId from the beginning of the list
  attrs.pop(0)
  # Append the proposalId to the end of the list
  attrs.append(proposalId)
  # Convert the list to a tuple
  values = tuple(attrs,)
  # Execute the query
  connect.cursor.execute(query, values)
  # Commit the changes
  connect.db.commit()
  # Print the message so the user knows the proposal has been updated
  print('Proposal updated successfully.')

# Define a function to delete a proposal receiving a proposalId
def delete(proposalId):
  # Define the query to delete a proposal
  query = 'DELETE FROM proposals WHERE id = %s'
  # Define the value to delete a proposal
  value = (proposalId,)
  # Execute the query
  connect.cursor.execute(query, value)
  # Commit the changes
  connect.db.commit()
  # Print the message so the user knows the proposal has been deleted
  print('Proposal has been deleted.')