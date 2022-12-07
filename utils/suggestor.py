"""
* Author: Matheus Carvalho, Amber Upton, Fatima Gonzales, Javier Segura, Sweastik Pokhrel
* Date: 12-06-2022
"""

INITIAL_VALUE = 68238.97
LARGE_COMPANY = 26558.22
SMALL_COMPANY = 10393.38
CONTRACT = 29201.57
MID_LEVEL = 46865.08
SENIOR_LEVEL = 82697
EXECUTIVE_LEVEL = 135930.3

# Define a function to get the company size values
def get_company_size(employees):
  # Check if the employees are less than 50
  if employees <= 49:
    # Return 'S' if the employees are less than 50
    return 'S'
  # Check if the employees are between 50 and 249
  if employees >= 50 and employees <= 249:
    # Return 'M' if the employees are between 50 and 249
    return 'M'
  # Return 'L' if the employees are greater than 250
  return 'L'

# Define a function to get the salary suggestion receiving a candidate and a company
def get_salary_suggestion(candidate, company):
  # Define the salary base value
  salary = INITIAL_VALUE
  # Get the company size
  companySize = get_company_size(int(company['employees']))

  # Check if the company size is 'L'
  if companySize == 'L':
    # Add the large company value to the salary
    salary += LARGE_COMPANY
  # Check if the company size is 'S'
  elif companySize == 'S':
    # Add the small company value to the salary
    salary += SMALL_COMPANY

  # Check if the experience level is 'MI'
  if candidate['experience_level'] == 'MI':
    # Add the mid level value to the salary
    salary += MID_LEVEL
  # Check if the experience level is 'SE'
  elif candidate['experience_level'] == 'SE':
    # Add the senior level value to the salary
    salary += SENIOR_LEVEL
  # Check if the experience level is 'EX'
  elif candidate['experience_level'] == 'EX':
    # Add the executive level value to the salary
    salary += EXECUTIVE_LEVEL

  # Check if the employment type is 'CT'
  if candidate['employment_type'] == 'CT':
    # Add the contract value to the salary
    salary += CONTRACT

  # Return the suggested salary
  return salary
