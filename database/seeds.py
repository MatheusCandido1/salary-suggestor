# Import connect from connect.py
import connect

# Define function to populate the companies table
def companies_seeder():
  # Define the query
  query = 'INSERT INTO companies (name, address, city, color, benefits, employees) VALUES (%s, %s, %s, %s, %s, %s)'
  # Define the values 
  values = (
    'UNLV', 
    '4505 S Maryland Pkwy', 
    'Las Vegas', 
    '#cf2030', 
    "Full family medical coverage will be provided through our company's employee benefit plan and will be effective on June 1. Dental and optical insurance are also available. The company offers a flexible paid time-off plan which includes vacation, personal and sick leave. Time off accrues at the rate of one day per month for your first year, then increased based on your tenure with the company. Eligibility for the company retirement plan begins 90 days after your start date",
    12000)
  # Execute the query
  connect.cursor.execute(query, values)
  # Commit the changes
  connect.db.commit()
  # Print the message so the user knows the database has been populated
  print('Seeds created successfully.')
