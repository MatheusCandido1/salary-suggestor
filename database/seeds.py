# Import connect from connect.py
import connect
# Import Faker
from faker import Faker
# Import random
import random

def seed():
  # Call the companies_seeder function
  companies_seeder()
  # Call the candidates_seeder function
  candidates_seeder()

# Define function to populate the companies table
def companies_seeder():
  # Define the query
  query = 'INSERT INTO companies (name, address, city, color, benefits, employees) VALUES (%s, %s, %s, %s, %s, %s)'
  # Define the values 
  values = [(
    'UNLV', 
    '4505 S Maryland Pkwy', 
    'Las Vegas', 
    '#cf2030', 
    "Full family medical coverage will be provided through our company's employee benefit plan and will be effective on June 1. Dental and optical insurance are also available. The company offers a flexible paid time-off plan which includes vacation, personal and sick leave. Time off accrues at the rate of one day per month for your first year, then increased based on your tenure with the company. Eligibility for the company retirement plan begins 90 days after your start date",
    12000
  ),
  (
    'Meta',
    'One Hacker Way',
    'Menlo Park',
    '#578bd1',
    "Full family medical coverage will be provided through our company's employee benefit plan and will be effective on June 1. Dental and optical insurance are also available. The company offers a flexible paid time-off plan which includes vacation, personal and sick leave. Time off accrues at the rate of one day per month for your first year, then increased based on your tenure with the company. Eligibility for the company retirement plan begins 90 days after your start date",
    40000
  ),
  (
    'Spotify',
    '150 Greenwich Street',
    'New York',
    '#59d955',
    "Full family medical coverage will be provided through our company's employee benefit plan and will be effective on June 1. Dental and optical insurance are also available. The company offers a flexible paid time-off plan which includes vacation, personal and sick leave. Time off accrues at the rate of one day per month for your first year, then increased based on your tenure with the company. Eligibility for the company retirement plan begins 90 days after your start date",
    25
  )
  ]
  # Loop through the values
  for value in values:
    # Execute the query
    connect.cursor.execute(query, value)
    # Commit the changes
    connect.db.commit()
  
  # Print the message so the user knows the database has been populated
  print('Companies created successfully.')

def candidates_seeder():
  # Define the query
  query = 'INSERT INTO candidates (name, address, email, phone, experience_level, employment_type) VALUES (%s, %s, %s, %s, %s, %s)'

  # Define the possible values for experience_level and employment_type
  experienceLevel = ['EN', 'MI', 'SE', 'EX']
  employmentType = ['FT', 'CT']
  # Create a Faker instance
  faker = Faker(locale='en_US')
  # Loop through the range of 1 to 201
  for i in range(1, 201):
    # Generate fake name
    fakeName = faker.name()
    # Generate fake address
    fakeAddress = faker.street_address()
    # Generate fake email and format it
    fakeEmail = fakeName.replace(' ', '').lower() + '@email.com'
    # Generate fake phone number
    fakePhone = faker.numerify(text='###-###-####')
    # Define the values getting a random value from experienceLevel and employmentType
    value = (
      fakeName,
      fakeAddress,
      fakeEmail,
      fakePhone,
      random.choice(experienceLevel),
      random.choice(employmentType),
    )
    # Execute the query
    connect.cursor.execute(query, value)
    # Commit the changes
    connect.db.commit()
    
  # Print the message so the user knows the database has been populated
  print('Candidates created successfully.')
