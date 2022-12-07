"""
* Author: Matheus Carvalho, Amber Upton, Fatima Gonzales, Javier Segura, Sweastik Pokhrel
* Date: 12-06-2022
"""
# Importing modules
import os
from controllers import company_controller, candidate_controller, proposal_controller
from utils import suggestor, pdf, statistics
import re

  # Define the master company
companyId = 1
  # Get the master company information from the database
masterCompany = company_controller.show(companyId)

# Define funciton to clear the terminal based on the OS
def clear_terminal():
  # For Windows
  if os.name == 'nt':
    os.system('cls')
  # For Mac and Linux
  else:
    os.system('clear')
# Define funciton to validate the hex color
def validate_hex_color(color):
  # Check if the color is a valid hex color
  if re.match(r'^#(?:[0-9a-fA-F]{3}){1,2}$', color):
    return True
  else:
    return False

# CANDIDATES
# Define funciton to get experience level label
def get_experience_level_label(value):
  if value == 'EN':
    return 'Entry Level'
  if value == 'MI':
    return 'Middle Level'
  if value == 'SE':
    return 'Senior Level'
  if value == 'EX':
    return 'Executive Level'
# Define funciton to get employment type label
def get_employment_type_label(value):
  if value == 'FT':
    return 'Full Time'
  if value == 'CT':
    return 'Contract'
# Define funciton to get experience level option
def get_experience_level(experience_level):
  if experience_level == 'EN':
     return '1'
  if experience_level == 'MI':
    return '2'
  if experience_level == 'SE':
    return '3'
  if experience_level == 'EX':
    return '4'

# Define funciton to get employment type option
def get_employment_type(employment_type):
  if employment_type == 'FT':
    return '1'
  if employment_type == 'CT':
    return '2'

# Define function to show candidates menu    
def show_candidates_menu():
  print ('\nManage Candidates\n')
  print ('1 - Create New Candidate')
  print ('2 - View Candidates')
  print ('3 - Update Existing Candidate')
  print ('4 - Delete Existing Candidate')
  print ('5 - Return to Main Menu\n')

# Define function to manage candidates
def update_candidate():
  # Get the candidate ID
  print('Please enter the ID of the candidate you wish to update.')
  candidateId = input()
  # Validate the candidate ID
  while candidateId == '':
    print('Candidate ID cannot be empty. Please enter again:')
    candidateId = input()
  # Get the candidate information from the database
  selectedCandidate = candidate_controller.show(candidateId)
  # Validate the candidate information
  if selectedCandidate:
    # Call the function to update the candidate
    update_existing_candidate(selectedCandidate)
  else:
    # Show error message
    print('Candidate not found.')

# Define function to delete candidate
def delete_candidate():
  # Get the candidate ID
  print('Please enter the ID of the candidate you wish to delete.')
  candidateId = input()
  # Validate the candidate ID
  while candidateId == '':
    print('Candidate ID cannot be empty. Please enter again:')
    candidateId = input()
  # Get the candidate information from the database
  currentCandidate = candidate_controller.show(candidateId)
  # Validate the candidate information
  if currentCandidate:
    # Print the candidate information
    print('Selected Candidate:')
    print('ID:'.ljust(18), currentCandidate[0])
    print('Name:'.ljust(18), currentCandidate[1])
    print('Address:'.ljust(18), currentCandidate[2])
    print('Email:'.ljust(18), currentCandidate[3])
    print('Phone:'.ljust(18), currentCandidate[4])
    print('Experience Level:'.ljust(18), get_experience_level_label(currentCandidate[5]))
    print('Employment Type:'.ljust(18), get_employment_type_label(currentCandidate[6]))
    # Ask for confirmation
    print('Are you sure you want to delete this candidate? (Y/N)')
    confirmation = input()
    # Validate the confirmation
    while confirmation not in ['Y', 'N', 'y', 'n']:
      print('Please enter a valid option:')
      confirmation = input()
    # Get validation option
    if confirmation == 'Y' or confirmation == 'y':
      # Call the function to delete the candidate
      candidate_controller.delete(candidateId)
  else:
    # Show error message
    print('Candidate not found.')
  # Call the function to manage candidates
  manage_candidates()

# Define function to create new candidate
def create_new_candidate():
  # Define the candidate dictionary
  candidate = {
    'name': '',
    'address': '',
    'email': '',
    'phone': '',
    'experience_level': '',
    'employment_type': ''
  }
  # Get the candidate's name
  print("Please enter candidate's name:")
  candidate['name'] = input()
  # Validate the candidate's name
  while candidate['name'] == '':
    print("Candidate's name cannot be empty.")
    print("Please enter candidate's name:")
    candidate['name'] = input()
  
  # Get the candidate's address
  print("Please enter candidate's address:")
  candidate['address'] = input()
  # Validate the candidate's address
  while candidate['address'] == '':
    print("Candidate's address cannot be empty.")
    print("Please enter candidate's address:")
    candidate['address'] = input()

  # Get the candidate's email     
  print("Please enter candidate's email:")
  candidate['email'] = input()
  # Validate the candidate's email
  while candidate['email'] == '':
    print("Candidate's email cannot be empty.")
    print("Please enter candidate's email:")
    candidate['email'] = input()
  
  # Get the candidate's phone
  print("Please enter candidate's phone number:")
  candidate['phone'] = input()
  # Validate the candidate's phone
  while candidate['phone'] == '':
    print("Candidate's phone number cannot be empty.")
    print("Please enter candidate's phone number:")
    candidate['phone'] = input()
  
  # Get the candidate's experience level
  print("Please enter candidate's experience level:")
  print('1 - Entry Level')
  print('2 - Middle Level')
  print('3 - Senior Level')
  print('4 - Executive Level')
  experienceLevelOption = input()
  # Validate the candidate's experience level
  while experienceLevelOption not in ['1', '2', '3', '4']:
    print ('Please enter a valid option:')
    experienceLevelOption = input()
  # Get the experience level option
  if experienceLevelOption == '1':
    candidate['experience_level'] = 'EN'
  elif experienceLevelOption == '2':
    candidate['experience_level'] = 'MI'
  elif experienceLevelOption == '3':
    candidate['experience_level'] = 'SE'
  else:
    candidate['experience_level'] = 'EX'
  
  # Get the candidate's employment type
  print("What is the candidate's preferred employment type?")
  print('1 - Full Time')
  print('2 - Contract')
  employmentTypeOption = input()
  # Validate the candidate's employment type
  while employmentTypeOption not in ['1', '2']:
    print ('Please enter a valid option:')
    employmentTypeOption = input()
  # Get the employment type option
  if employmentTypeOption == '1':
    candidate['employment_type'] = 'FT'
  else:
    candidate['employment_type'] = 'CT'
  # Call the function to store the candidate
  candidate_controller.store(candidate)
  # Call the function to manage candidates
  manage_candidates()
    
# Define function to view candidates
def view_candidates():
  # Call the function to get the candidates
  result = candidate_controller.index()
  # Check if there are candidates
  if len(result) == 0:
    # If there are no candidates, show error message
    print('There are no candidates.')
  # Print the candidates
  else:
    # Print header
    print("ID".ljust(3), "Name".ljust(35), "Address".ljust(35), "Email".ljust(35), "Phone".ljust(14), "Experience Level".ljust(16), "Employment Time".ljust(10))
    print('----------------------------------------------------------------------------------------------------------------------------------------------------------------')
    # Loop through the candidates and print them
    for candidate in result:
      print(str(candidate[0]).ljust(3), str(candidate[1]).ljust(35), str(candidate[2]).ljust(35), str(candidate[3]).ljust(35), str(candidate[4]).ljust(14), str(get_experience_level_label(candidate[5])).ljust(16), str(get_employment_type_label(candidate[6])).ljust(10))
  # Call the function to manage candidates
  manage_candidates()
    
# Define function to update candidate
def update_existing_candidate(candidate): 
  # Define the updated candidate dictionary 
  updatedCandidate = {
    'id': candidate[0],
    'name': candidate[1],
    'address': candidate[2],
    'email': candidate[3],
    'phone': candidate[4],
    'experience_level': candidate[5],
    'employment_type': candidate[6]
  }
  # Print the current candidate information
  print('Current Candidate Information: ')
  print('Name: '.ljust(18), candidate[1])
  print('Address: '.ljust(18), candidate[2])
  print('Email: '.ljust(18), candidate[3])
  print('Phone: '.ljust(18), candidate[4])
  print('Experience Level:'.ljust(18), get_experience_level_label(candidate[5]))
  print('Employment Type:'.ljust(18), get_employment_type_label(candidate[6]))
  # Get the updated candidate information
  # If the user doesn't want to update a field, the current value will be used
  # If the user wants to update a field, the new value will be used
  updatedCandidate['name'] = input("Candidate Name: (press enter if you don't want to update) ") or candidate[1]
  updatedCandidate['address'] = input("Candidate Address: (press enter if you don't want to update) ") or candidate[2]
  updatedCandidate['email'] = input("Candidate Email: (press enter if you don't want to update) ") or candidate[3]
  updatedCandidate['phone'] = input("Candidate Phone: (press enter if you don't want to update) ") or candidate[4]
  print("If updating candidate's experience level, please enter appropriate option:")
  print('1 - Entry Level')
  print('2 - Middle Level')
  print('3 - Senior Level')
  print('4 - Executive Level')
  experienceLevelOption  = input("Candidate Experience Level: (press enter if you don't want to update) ") or get_experience_level(candidate[5])
  while experienceLevelOption not in ['1', '2', '3', '4']:
    print ('Please enter a valid option:')
    experienceLevelOption = input()
  if experienceLevelOption == '1':
    updatedCandidate['experience_level'] = 'EN'
  elif experienceLevelOption == '2':
    updatedCandidate['experience_level'] = 'MI'
  elif experienceLevelOption == '3':
    updatedCandidate['experience_level'] = 'SE'
  else:
    updatedCandidate['experience_level'] = 'EX'
    
  print("If updating the candidate's preffered employment type.")
  print('1 - Full Time')
  print('2 - Contract')
  employmentTypeOption = input("Candidate Employment Type: (press enter if you don't want to update) ") or get_employment_type(candidate[6])
  while employmentTypeOption not in ['1', '2']:
    print ('Please enter a valid option:')
    employmentTypeOption = input()
  if employmentTypeOption == '1':
    updatedCandidate['employment_type'] = 'FT'
  else:
    updatedCandidate['employment_type'] = 'CT'
  # Call the function to update the candidate
  candidate_controller.update(updatedCandidate)
  # Call the function to manage candidates
  manage_candidates()
    
# Define function to show main menu
def go_back():
  # Call the main function
  bootstrap()

# Define function to manage candidates
def manage_candidates():
  # Call the function to show the candidates menu
  show_candidates_menu()
  # beginning of main program
  # have user enter the corresponding number of the option they want to execute
  print ('Please enter the option:')
  option = input()
      
  # validate the option
  while option not in ['1', '2', '3', '4', '5']:
    print ('Please enter a valid option:')
    option = input()

  # execute the option
  if option == '1':
    create_new_candidate()
  elif option == '2':
    view_candidates()
  elif option == '3':
    update_candidate()
  elif option == '4':
    delete_candidate()
  else:
    go_back()

# PROPOSALS
# Define function to get status label
def get_status(status):
  if status == 'PENDING':
    return '1'
  if status == 'ACCEPTED':
    return '2'
  if status == 'DECLINED':
    return '3'

# Define function to format salary as currency
def format_salary(salary):
  return '${:,.2f}'.format(salary)

# Define function to get salary suggestion
def get_salary_suggestion(candidate, company):
  # Call the function to get salary suggestion and store it in a variable
  value = suggestor.get_salary_suggestion(candidate, company)
  # Return the value
  return value

# Define funciton to create new proposal
def create_new_proposal(company):
  # Get the candidate ID
  candidateId = input('Please enter the ID of the candidate: ')
  # Validate the candidate ID
  while candidateId == '':
    print('ID of the candidate cannot be empty.')
    candidateId = input('Please enter the ID of the candidate: ')
  # Call the function to get the candidate and store it in a variable
  candidate = candidate_controller.show(candidateId)
  # Validate the candidate
  if not candidate:
    print('Candidate not found.')
  else:
    # Print the candidate information
    print('\nSelected Candidate Information: ')
    print('Name: '.ljust(18), candidate[1])
    print('Address: '.ljust(18), candidate[2])
    print('Email: '.ljust(18), candidate[3])
    print('Phone: '.ljust(18), candidate[4])
    print('Experience Level: '.ljust(18), get_experience_level_label(candidate[5]))
    print('Employment Type:'.ljust(18), get_employment_type_label(candidate[6]))
    print('\nCreate New Proposal\n')
    
    # Create a new proposal dictionary
    proposal = {
      'candidate_id': candidateId,
      'job_title': '',
      'salary': '',
      'status': 'PENDING'
    }
    
    # Get the job title
    print('Please enter the job title:')
    proposal['job_title'] = input()

    # Validate the job title
    if proposal['job_title'] == '':
      print('Job title cannot be empty.')
      proposal['job_title'] = input()

    # Create company dictionary
    selectedCompany = {
      'employees': company[6],
    }

    # Create candidate dictionary
    selectedCandidate = {
      'experience_level': candidate[5],
      'employment_type': candidate[6],
    }
    # Call the function to get salary suggestion passing the candidate and company information and store it in a variable 
    salarySuggestion = get_salary_suggestion(selectedCandidate, selectedCompany)
    # Print the salary suggestion
    print('For this candidate, we suggest a salary of ' + str(format_salary(salarySuggestion)) + '.')
    # If the user wants to accept the suggested salary, press enter. Otherwise, enter the salary you want to propose.
    proposal['salary'] = input('If you want to accept the suggested salary, press enter. Otherwise, enter the salary you want to propose.') or salarySuggestion
    if proposal['salary'] == '':
      print('Salary cannot be empty.')
      proposal['salary'] = input()

    # Validate if salary is less than the suggested
    if float(proposal['salary']) < salarySuggestion:
      # Ask the user if they want to continue
      print('The salary you entered is less than the suggested. Are you sure you want to continue? (Y/N)')
      confirmation = input()
      # Validate the confirmation
      while confirmation not in ['Y', 'y', 'N', 'n']:
        print('Please enter a valid option: (Y/N)')
        confirmation = input()
      # If the user does not want to continue, call the function to manage proposals
      if confirmation in ['N', 'n']:
        # Call the function to manage proposals
        manage_proposals(selectedCompany)
      # If the user wants to continue, call the function to store the proposal
    proposal_controller.store(proposal)
  # Call the function to manage proposals
  manage_proposals(masterCompany)

# Define function to delete proposals
def delete_proposal():
  # Get the proposal ID
  print('Please enter the ID of the proposal you wish to delete.')
  proposalId = input()
  # Validate the proposal ID
  while proposalId == '':
    print('Proposal ID cannot be empty. Please enter again:')
    proposalId = input()
  # Call the function to get the proposal and store it in a variable
  currentProposal = proposal_controller.show(proposalId)
  # Validate the proposal
  if currentProposal:
    # Print the proposal information
    print('\nSelected Proposal Information: ')
    print('ID: '.ljust(18), currentProposal[1])
    print('Candidate Name: '.ljust(18), currentProposal[6])
    print('Proposal Date: '.ljust(18), currentProposal[2].strftime("%B %d, %Y"))
    print('Job Title: '.ljust(18), currentProposal[3])
    print('Salary Offered: '.ljust(18), format_salary(currentProposal[4]))

    # Ask for confirmation
    print('Are you sure you want to delete this proposal? (Y/N)')
    confirmation = input()

    # Validate the confirmation
    while confirmation not in ['Y', 'y', 'N', 'n']:
      print('Please enter a valid option: (Y/N)')
      confirmation = input()
    # If the user wants to delete the proposal, call the function to delete the proposal
    if confirmation in ['Y', 'y']:
      # Call the function to delete the proposal
      proposal_controller.delete(proposalId)
  else:
    # Print the message if the proposal is not found
    print('Proposal not found.')
  # Call the function to manage proposals
  manage_proposals(masterCompany)

# Define function to view proposals
def view_proposal(company):
  # Call the function to get all proposals and store it in a variable
  proposals = proposal_controller.index()
  # Validate if there are proposals
  if len(proposals) == 0:
    # Print the message if there are no proposals
    print('There are no proposals.')

  # Print the proposals
  else:
    # Print the header
    print("Proposal ID".ljust(11), "Candidate".ljust(30), "Proposal Date".ljust(20), "Salary Offered".ljust(20), "Status".ljust(20))
    print('---------------------------------------------------------------------------------------------')
    # Loop through the proposals
    for proposal in proposals:
      print(str(proposal[0]).ljust(11), proposal[6].ljust(30), proposal[2].strftime("%B %d, %Y").ljust(20), str(format_salary(proposal[4]).ljust(20)), proposal[5].ljust(20))
  
  # Get the proposal ID
  print('\nPlease enter the ID of the proposal you wish to view (or enter 0 to go back).')
  # Validate the proposal ID
  proposalId = input()
  while proposalId == '':
    print('Proposal ID cannot be empty. Please enter again:')
    proposalId = input()
  # Call the function to manage proposals if the user wants to go back
  if proposalId == '0':
    manage_proposals(company)
  # Call the function to get the proposal and store it in a variable
  currentProposal = proposal_controller.show(proposalId)
  # Validate the proposal
  if currentProposal:
    # Print the proposal information
    print('\nSelected Proposal Information: ')
    print('ID: '.ljust(18), currentProposal[0])
    print('Candidate Name: '.ljust(18), currentProposal[6])
    print('Proposal Date: '.ljust(18), currentProposal[2].strftime("%B %d, %Y"))
    print('Job Title: '.ljust(18), currentProposal[3])
    print('Salary Offered: '.ljust(18), currentProposal[4])
    print('Status: '.ljust(18), currentProposal[5])

    # Ask if the user wants to generate a PDF
    print('Would you like to visualize this proposal as a PDF? (Y/N)')
    confirmation = input()
    
    # Validate the confirmation
    while confirmation not in ['Y', 'y', 'N', 'n']:
      print('Please enter a valid option: (Y/N)')
      confirmation = input()
    # If the user wants to generate a PDF, call the function to generate the PDF
    if confirmation in ['Y', 'y']:
      # Print the message
      print('Generating PDF...')

      # Create company dictionary with the information to be passed to the PDF generator
      selectedCompany = {
        'name': company[1],
        'address': company[2],
        'city': company[3],
        'color': company[4],
        'benefits': company[5],
      }

      # Create candidate dictionary with the information to be passed to the PDF generator
      selectedCandidate = {
        'name': currentProposal[6],
      }

      # Create proposal dictionary with the information to be passed to the PDF generator
      selectedProposal = {
        'job_title': currentProposal[3],
        'salary': currentProposal[4],
        'proposal_date': currentProposal[2],
      }
      
      # Call the function to generate the PDF
      pdf.generate(selectedCompany, selectedCandidate, selectedProposal)
  else:
    # Print the message if the proposal is not found
    print('Proposal not found.')
  # Call the function to manage proposals
  manage_proposals(masterCompany)

# Define function to update proposals
def update_existing_proposal():
  # Get the proposal ID
  print('Please enter the ID of the proposal you wish to update.')
  proposalId = input()
  # Validate the proposal ID
  while proposalId == '':
    print('Proposal ID cannot be empty. Please enter again:')
    proposalId = input()
  # Call the function to get the proposal and store it in a variable
  currentProposal = proposal_controller.show(proposalId)
  # Validate the proposal
  if currentProposal:
    # Print the proposal information
    print('\nSelected Proposal Information: ')
    print('Proposal ID: '.ljust(18), currentProposal[0])
    print('Candidate ID: '.ljust(18), currentProposal[1])
    print('Proposal Date: '.ljust(18), currentProposal[2].strftime("%B %d, %Y"))
    print('Job Title: '.ljust(18), currentProposal[3])
    print('Salary Offered: '.ljust(18), format_salary(currentProposal[4]))
    print('Status: '.ljust(18), currentProposal[5])

    # Create a dictionary with the current proposal information
    updatedProposal = {
      'id': currentProposal[0],
      'candidate_id': currentProposal[1],
      'job_title': currentProposal[3],
      'salary': currentProposal[4],
      'status': currentProposal[5]
    }

    # Get the updated proposal information
    # If the user doesn't want to update a field, the current value will be used
    # If the user wants to update a field, the new value will be used
    updatedProposal['job_title'] = input("Job Title: (press enter if you don't want to update) ") or currentProposal[3]
    updatedProposal['salary'] = input("Salary: (press enter if you don't want to update) ") or currentProposal[4]
    print("If updating proposals's status, please enter appropriate option:")
    print('1 - PENDING')
    print('2 - ACCEPTED')
    print('3 - DECLINED')
    statusOption = input("Status: (press enter if you don't want to update) ") or get_status(currentProposal[5])
    while statusOption not in ['1', '2', '3']:
      print ('Please enter a valid option:')
      statusOption = input()
    if statusOption == '1':
        updatedProposal['status'] = 'PENDING'
    elif statusOption == '2':
        updatedProposal['status'] = 'ACCEPTED'
    else:
        updatedProposal['status'] = 'DECLINED'
    proposal_controller.update(updatedProposal)

  else:
    # Print the message if the proposal is not found
    print('Proposal not found.')
  # Call the function to manage proposals
  manage_proposals(masterCompany)
  
# Define function to show the proposals menu
def show_proposals_menu():
    print ('\nManage Proposals\n')
    print ('1 - Create New Proposal')
    print ('2 - View Proposals')
    print ('3 - Update Existing Proposal')
    print ('4 - Delete Existing Proposal')
    print ('5 - Return to Main Menu\n')
# Define function to manage proposals
def manage_proposals(company):
  # Call the function to show the proposals menu
  show_proposals_menu()
  # Get the option from the user
  print ('Please enter the option:')
  option = input()

  # Validate the option
  while option not in ['1', '2', '3', '4', '5']:
      print ('Please enter a valid option:')
      option = input()
  # Call option that the user selected
  if option == '1':
    create_new_proposal(company)
  elif option == '2':
    view_proposal(company)
  elif option == '3':
    update_existing_proposal()
  elif option == '4':
    delete_proposal()
  else:
    go_back()

# COMPANIES
# Define function to show the companies menu
def show_companies_menu():
    print('\nManage Company\n')
    print('1 - Update Company Information')
    print('2 - Return to Main Menu\n')

# Define function to show company information
def view_company():
  print('\nCompany Information:')
  print('Name:'.ljust(8) , masterCompany[1])
  print('Address:'.ljust(8), masterCompany[2])
  print('City:'.ljust(8), masterCompany[3])
  print('Color:'.ljust(8), masterCompany[4])

# Define function to update company information
def update_company():
  # Print the company information
  print('\nCompany Information:')
  print('Name:'.ljust(8) , masterCompany[1])
  print('Address:'.ljust(8), masterCompany[2])
  print('City:'.ljust(8), masterCompany[3])
  print('Color:'.ljust(8), masterCompany[4])

  # Create a dictionary with the current company information
  updatedCompany = {
    'id': masterCompany[0],
    'name': masterCompany[1],
    'address': masterCompany[2],
    'city': masterCompany[3],
    'color': masterCompany[4],
    'benefits': masterCompany[5]
  }
  # Get the updated company information
  # If the user doesn't want to update a field, the current value will be used
  # If the user wants to update a field, the new value will be used
  updatedCompany['name'] = input("Name: (press enter if you don't want to update) ") or masterCompany[1]
  updatedCompany['address'] = input("Address: (press enter if you don't want to update) ") or masterCompany[2]
  updatedCompany['city'] = input("City: (press enter if you don't want to update) ") or masterCompany[3]
  updatedCompany['color'] = input("Color: (press enter if you don't want to update) ") or masterCompany[4]
  # Validate the color
  if not validate_hex_color(updatedCompany['color']):
    print('Invalid color. Please enter a valid hex color.')
    updatedCompany['color'] = input("Color: (press enter if you don't want to update) ") or masterCompany[4]
  updatedCompany['benefits'] = input("Benefits: (press enter if you don't want to update) ") or masterCompany[5]
  # Call the function to update the company
  company_controller.update(updatedCompany)
  # Call the function to manage companies
  manage_companies()

# Define function to manage companies
def manage_companies():
  # Call the function to show company information
  view_company()
  # Call the function to show the companies menu
  show_companies_menu()

  # Get the option from the user
  print ('Please enter the option:')
  option = input()

  # Validate the option
  while option not in ['1', '2', '3']:
      print ('Please enter a valid option:')
      option = input()
  # Call option that the user selected
  if option == '1':
    update_company()
  else:
    go_back()

# STATISTICS
# Define function to show the statistics menu
def display_statistics():
  # Call the function to generate the statistics
  statistics.generate_statistics()

  # Print the statistics menu
  print('\n1 - Generate Chart')
  print('2 - Return to Main Menu\n')

  # Get the option from the user
  print ('Please enter the option:')
  option = input()
  # Validate the option
  while option not in ['1', '2']:
    print ('Please enter a valid option:')
    option = input()

  # Call option that the user selected
  if option == '1':
    statistics.generate_chart()
    
  go_back()

# MAIN APPLICATION
# Define function to show the main menu
def show_main_menu():
  # Print the main menu
  print('\nMenu:')
  print('1 - Manage Company')
  print('2 - Manage Candidates')
  print('3 - Manage Proposals')
  print('4 - Display Statistics')
  print('5 - Exit \n')

# Define main funciton
def bootstrap():
  # Call the function to clear the terminal
  clear_terminal()

  # Print welcome message
  print('Welcome to the Salary Suggestor')

  # Call the function to show the main menu
  show_main_menu()

  # Get the option from the user
  print ('Please enter the option:')
  option = input()

  # Validate the option
  while option not in ['1', '2', '3', '4', '5']:
    print('Please enter a valid option:')
    show_main_menu()
    option = input()

  # Call option that the user selected
  if option == '1':
    manage_companies()
  if option == '2':
    manage_candidates()
  if option == '3':
    manage_proposals(masterCompany)
  if option == '4':
    display_statistics()
  if option == '5':
    print('Thank you for using the Data Salary Calculator! Session has ended.')
    exit()

# Call the main function
bootstrap()