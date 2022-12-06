"""
* Author: Matheus Carvalho, Amber Upton, Fatima Gonzales, Javier Segura, Sweastik Pokhrel
* Date: 12-03-2022
"""
import os
from controllers import company_controller, candidate_controller, proposal_controller
from utils import suggestor, pdf, statistics

def clear_terminal():
  if os.name == 'nt':
    os.system('cls')
  else:
    os.system('clear')


companyId = 1
masterCompany = company_controller.show(companyId)

# CANDIDATES
def get_experience_level_label(value):
  if value == 'EN':
    return 'Entry Level'
  if value == 'MI':
    return 'Middle Level'
  if value == 'SE':
    return 'Senior Level'
  if value == 'EX':
    return 'Executive Level'

def get_employment_type_label(value):
  if value == 'FT':
    return 'Full Time'
  if value == 'CT':
    return 'Contract'

def get_experience_level(experience_level):
  if experience_level == 'EN':
     return '1'
  if experience_level == 'MI':
    return '2'
  if experience_level == 'SE':
    return '3'
  if experience_level == 'EX':
    return '4'

def get_employment_type(employment_type):
  if employment_type == 'FT':
    return '1'
  if employment_type == 'CT':
    return '2'
    
def show_candidates_menu():
  print ('\nManage Candidates\n')
  print ('1 - Create New Candidate')
  print ('2 - View Candidates')
  print ('3 - Update Existing Candidate')
  print ('4 - Delete Existing Candidate')
  print ('5 - Return to Main Menu\n')

def update_candidate():
  print('Please enter the ID of the candidate you wish to update.')
  candidateId = input()
  while candidateId == '':
    print('Candidate ID cannot be empty. Please enter again:')
    candidateId = input()
  selectedCandidate = candidate_controller.show(candidateId)
  if selectedCandidate:
    update_existing_candidate(selectedCandidate)
  else:
    print('Candidate not found.')

def delete_candidate():
  print('Please enter the ID of the candidate you wish to delete.')
  candidateId = input()
  while candidateId == '':
    print('Candidate ID cannot be empty. Please enter again:')
    candidateId = input()
  currentCandidate = candidate_controller.show(candidateId)
  if currentCandidate:
    print('Selected Candidate:')
    print('ID:'.ljust(18), currentCandidate[0])
    print('Name:'.ljust(18), currentCandidate[1])
    print('Address:'.ljust(18), currentCandidate[2])
    print('Email:'.ljust(18), currentCandidate[3])
    print('Phone:'.ljust(18), currentCandidate[4])
    print('Experience Level:'.ljust(18), get_experience_level_label(currentCandidate[5]))
    print('Employment Type:'.ljust(18), get_employment_type_label(currentCandidate[6]))
    print('Are you sure you want to delete this candidate? (Y/N)')
    confirmation = input()
    while confirmation not in ['Y', 'N', 'y', 'n']:
      print('Please enter a valid option:')
      confirmation = input()
    if confirmation == 'Y' or confirmation == 'y':
      candidate_controller.delete(candidateId)
  else:
    print('Candidate not found.')
  manage_candidates()

def create_new_candidate():
  candidate = {
    'name': '',
    'address': '',
    'email': '',
    'phone': '',
    'experience_level': '',
    'employment_type': ''
  }
    
  print("Please enter candidate's name:")
  candidate['name'] = input()
  while candidate['name'] == '':
    print("Candidate's name cannot be empty.")
    print("Please enter candidate's name:")
    candidate['name'] = input()
        
  print("Please enter candidate's address:")
  candidate['address'] = input()
  while candidate['address'] == '':
    print("Candidate's address cannot be empty.")
    print("Please enter candidate's address:")
    candidate['address'] = input()
        
  print("Please enter candidate's email:")
  candidate['email'] = input()
  while candidate['email'] == '':
    print("Candidate's email cannot be empty.")
    print("Please enter candidate's email:")
    candidate['email'] = input()
        
  print("Please enter candidate's phone number:")
  candidate['phone'] = input()
  while candidate['phone'] == '':
    print("Candidate's phone number cannot be empty.")
    print("Please enter candidate's phone number:")
    candidate['phone'] = input()
        
  print("Please enter candidate's experience level:")
  print('1 - Entry Level')
  print('2 - Middle Level')
  print('3 - Senior Level')
  print('4 - Executive Level')
  experienceLevelOption = input()
  while experienceLevelOption not in ['1', '2', '3', '4']:
    print ('Please enter a valid option:')
    experienceLevelOption = input()
  if experienceLevelOption == '1':
    candidate['experience_level'] = 'EN'
  elif experienceLevelOption == '2':
    candidate['experience_level'] = 'MI'
  elif experienceLevelOption == '3':
    candidate['experience_level'] = 'SE'
  else:
    candidate['experience_level'] = 'EX'
        
  print("What is the candidate's preferred employment type?")
  print('1 - Full Time')
  print('2 - Contract')
  employmentTypeOption = input()
  while employmentTypeOption not in ['1', '2']:
    print ('Please enter a valid option:')
    employmentTypeOption = input()
  if employmentTypeOption == '1':
    candidate['employment_type'] = 'FT'
  else:
    candidate['employment_type'] = 'CT'
  candidate_controller.store(candidate)
  manage_candidates()
    
def view_candidates():
  result = candidate_controller.index()
  if len(result) == 0:
    print('There are no candidates.')
  else:
    print("ID".ljust(3), "Name".ljust(20), "Address".ljust(20), "Email".ljust(20), "Phone".ljust(12), "Experience Level".ljust(2), "Employment Time".ljust(3))
    print('------------------------------------------------------------------------------------------------------------------------')
    for candidate in result:
      print(str(candidate[0]).ljust(3), str(candidate[1]).ljust(20), str(candidate[2]).ljust(20), str(candidate[3]).ljust(20), str(candidate[4]).ljust(12), str(get_experience_level_label(candidate[5])).ljust(16), str(get_employment_type_label(candidate[6])).ljust(3))
  manage_candidates()
    
def update_existing_candidate(candidate):  
  updatedCandidate = {
    'id': candidate[0],
    'name': candidate[1],
    'address': candidate[2],
    'email': candidate[3],
    'phone': candidate[4],
    'experience_level': candidate[5],
    'employment_type': candidate[6]
  }
  print('Current Candidate Information: ')
  print('Name: '.ljust(18), candidate[1])
  print('Address: '.ljust(18), candidate[2])
  print('Email: '.ljust(18), candidate[3])
  print('Phone: '.ljust(18), candidate[4])
  print('Experience Level:'.ljust(18), get_experience_level_label(candidate[5]))
  print('Employment Type:'.ljust(18), get_employment_type_label(candidate[6]))
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

  candidate_controller.update(updatedCandidate)
    
def go_back():
  bootstrap()

def manage_candidates():
  show_candidates_menu()
  # beginning of main program
  # have user enter the corresponding number of the option they want to execute
  print ('Please enter the option:')
  option = input()
      
  # input validation: make sure user enters 
  while option not in ['1', '2', '3', '4', '5']:
    print ('Please enter a valid option:')
    option = input()

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
def get_status(status):
  if status == 'PENDING':
    return '1'
  if status == 'ACCEPTED':
    return '2'
  if status == 'DECLINED':
    return '3'


def format_salary(salary):
  return '${:,.2f}'.format(salary)

def get_salary_suggestion(candidate, company):
  value = suggestor.get_salary_suggestion(candidate, company)
  return value

def create_new_proposal(company):
  candidateId = input('Please enter the ID of the candidate: ')
  while candidateId == '':
    print('ID of the candidate cannot be empty.')
    candidateId = input('Please enter the ID of the candidate: ')

  candidate = candidate_controller.show(candidateId)
  if not candidate:
    print('Candidate not found.')
  else:
    print('\nSelected Candidate Information: ')
    print('Name: '.ljust(18), candidate[1])
    print('Address: '.ljust(18), candidate[2])
    print('Email: '.ljust(18), candidate[3])
    print('Phone: '.ljust(18), candidate[4])
    print('Experience Level: '.ljust(18), get_experience_level_label(candidate[5]))
    print('Employment Type:'.ljust(18), get_employment_type_label(candidate[6]))
    print('\nCreate New Proposal\n')

    proposal = {
      'candidate_id': candidateId,
      'job_title': '',
      'salary': '',
      'status': 'PENDING'
    }

    print('Please enter the job title:')
    proposal['job_title'] = input()

    if proposal['job_title'] == '':
      print('Job title cannot be empty.')
      proposal['job_title'] = input()

    selectedCompany = {
      'employees': company[6],
    }

    selectedCandidate = {
      'experience_level': candidate[5],
      'employment_type': candidate[6],
    }

    salarySuggestion = get_salary_suggestion(selectedCandidate, selectedCompany)
    print('For this candidate, we suggest a salary of ' + str(format_salary(salarySuggestion)) + '.')

    proposal['salary'] = input('If you want to accept the suggested salary, press enter. Otherwise, enter the salary you want to propose.') or salarySuggestion
    if proposal['salary'] == '':
      print('Salary cannot be empty.')
      proposal['salary'] = input()

    if float(proposal['salary']) < salarySuggestion:
      print('The salary you entered is less than the suggested. Are you sure you want to continue? (Y/N)')
      confirmation = input()
      while confirmation not in ['Y', 'y', 'N', 'n']:
        print('Please enter a valid option: (Y/N)')
        confirmation = input()
      if confirmation in ['N', 'n']:
        manage_proposals(selectedCompany)

    proposal_controller.store(proposal)
  manage_proposals(masterCompany)

def delete_proposal():
  print('Please enter the ID of the proposal you wish to delete.')
  proposalId = input()
  while proposalId == '':
    print('Proposal ID cannot be empty. Please enter again:')
    proposalId = input()

  currentProposal = proposal_controller.show(proposalId)
  if currentProposal:
    print('\nSelected Proposal Information: ')
    print('ID: '.ljust(18), currentProposal[1])
    print('Candidate Name: '.ljust(18), currentProposal[6])
    print('Proposal Date: '.ljust(18), currentProposal[2].strftime("%B %d, %Y"))
    print('Job Title: '.ljust(18), currentProposal[3])
    print('Salary Offered: '.ljust(18), format_salary(currentProposal[4]))

    print('Are you sure you want to delete this proposal? (Y/N)')
    confirmation = input()
    while confirmation not in ['Y', 'y', 'N', 'n']:
      print('Please enter a valid option: (Y/N)')
      confirmation = input()
    if confirmation in ['Y', 'y']:
      proposal_controller.delete(proposalId)
  else:
    print('Proposal not found.')
  manage_proposals(masterCompany)

def view_proposal(company):
  proposals = proposal_controller.index()
  if len(proposals) == 0:
    print('There are no proposals.')
  else:
    print("Proposal ID".ljust(11), "Candidate".ljust(20), "Proposal Date".ljust(20), "Salary Offered".ljust(20), "Status".ljust(20))
    print('---------------------------------------------------------------------------------------------')
    for proposal in proposals:
      print(str(proposal[0]).ljust(11), proposal[6].ljust(20), proposal[2].strftime("%B %d, %Y").ljust(20), str(format_salary(proposal[4]).ljust(20)), proposal[5].ljust(20))
  
  
  print('\nPlease enter the ID of the proposal you wish to view (or enter 0 to go back).')
  proposalId = input()
  while proposalId == '':
    print('Proposal ID cannot be empty. Please enter again:')
    proposalId = input()
  if proposalId == '0':
    manage_proposals(company)
  currentProposal = proposal_controller.show(proposalId)
  if currentProposal:
    print('\nSelected Proposal Information: ')
    print('ID: '.ljust(18), currentProposal[0])
    print('Candidate Name: '.ljust(18), currentProposal[6])
    print('Proposal Date: '.ljust(18), currentProposal[2].strftime("%B %d, %Y"))
    print('Job Title: '.ljust(18), currentProposal[3])
    print('Salary Offered: '.ljust(18), currentProposal[4])
    print('Status: '.ljust(18), currentProposal[5])

    print('Would you like to visualize this proposal as a PDF? (Y/N)')
    confirmation = input()

    while confirmation not in ['Y', 'y', 'N', 'n']:
      print('Please enter a valid option: (Y/N)')
      confirmation = input()
    if confirmation in ['Y', 'y']:
      print('Generating PDF...')
      selectedCompany = {
        'name': company[1],
        'address': company[2],
        'city': company[3],
        'color': company[4],
        'benefits': company[5],
      }
      selectedCandidate = {
        'name': currentProposal[6],
      }
      selectedProposal = {
        'job_title': currentProposal[3],
        'salary': currentProposal[4],
        'proposal_date': currentProposal[2],
      }

      pdf.generate(selectedCompany, selectedCandidate, selectedProposal)
  else:
    print('Proposal not found.')
  manage_proposals(masterCompany)

def update_existing_proposal():
  print('Please enter the ID of the proposal you wish to update.')
  proposalId = input()
  while proposalId == '':
    print('Proposal ID cannot be empty. Please enter again:')
    proposalId = input()

  currentProposal = proposal_controller.show(proposalId)
  if currentProposal:
    print('\nSelected Proposal Information: ')
    print('ID: '.ljust(18), currentProposal[1])
    print('Proposal Date: '.ljust(18), currentProposal[2].strftime("%B %d, %Y"))
    print('Job Title: '.ljust(18), currentProposal[3])
    print('Salary Offered: '.ljust(18), currentProposal[4])
    print('Status: '.ljust(18), currentProposal[5])

    updatedProposal = {
      'id': currentProposal[0],
      'candidate_id': currentProposal[1],
      'proposal_date': currentProposal[2],
      'job_title': currentProposal[3],
      'salary': currentProposal[4],
      'status': currentProposal[5]
    }

    updatedProposal['proposal_date'] = input("Proposal Date: (press enter if you don't want to update) ") or currentProposal[2]
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
    print('Proposal not found.')

  manage_proposals(masterCompany)
  
def show_proposals_menu():
    print ('\nManage Proposals\n')
    print ('1 - Create New Proposal')
    print ('2 - View Proposals')
    print ('3 - Update Existing Proposal')
    print ('4 - Delete Existing Proposal')
    print ('5 - Return to Main Menu\n')

def manage_proposals(company):
  show_proposals_menu()

  print ('Please enter the option:')
  option = input()
      
  while option not in ['1', '2', '3', '4', '5']:
      print ('Please enter a valid option:')
      option = input()
  
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
def show_companies_menu():
    print('\nManage Company\n')
    print('1 - Update Company Information')
    print('2 - Return to Main Menu\n')

def view_company():
  print('\nCompany Information:')
  print('Name:'.ljust(8) , masterCompany[1])
  print('Address:'.ljust(8), masterCompany[2])
  print('City:'.ljust(8), masterCompany[3])
  print('Color:'.ljust(8), masterCompany[4])

def update_company():
  print('\nCompany Information:')
  print('Name:'.ljust(8) , masterCompany[1])
  print('Address:'.ljust(8), masterCompany[2])
  print('City:'.ljust(8), masterCompany[3])
  print('Color:'.ljust(8), masterCompany[4])

  updatedCompany = {
    'id': masterCompany[0],
    'name': masterCompany[1],
    'address': masterCompany[2],
    'city': masterCompany[3],
    'color': masterCompany[4],
    'benefits': masterCompany[5]
  }

  updatedCompany['name'] = input("Name: (press enter if you don't want to update) ") or masterCompany[1]
  updatedCompany['address'] = input("Address: (press enter if you don't want to update) ") or masterCompany[2]
  updatedCompany['city'] = input("City: (press enter if you don't want to update) ") or masterCompany[3]
  updatedCompany['color'] = input("Color: (press enter if you don't want to update) ") or masterCompany[4]
  updatedCompany['benefits'] = input("Benefits: (press enter if you don't want to update) ") or masterCompany[5]

  company_controller.update(updatedCompany)
  manage_companies()


def manage_companies():
  view_company()
  show_companies_menu()

  print ('Please enter the option:')
  option = input()
      
  while option not in ['1', '2', '3']:
      print ('Please enter a valid option:')
      option = input()
  
  if option == '1':
    update_company()
  else:
    go_back()

# STATISTICS
def display_statistics():
  statistics.generate_statistics()

  print('\n1 - Generate Chart')
  print('2 - Return to Main Menu\n')

  print ('Please enter the option:')
  option = input()
  while option not in ['1', '2']:
    print ('Please enter a valid option:')
    option = input()
  
  if option == '1':
    statistics.generate_chart()
    
  go_back()

# MAIN APPLICATION
def show_main_menu():
  print('\nMenu:')
  print('1 - Manage Company')
  print('2 - Manage Candidates')
  print('3 - Manage Proposals')
  print('4 - Display Statistics')
  print('5 - Exit \n')

def bootstrap():
  clear_terminal()

  print('Welcome to the Salary Suggestor')
  show_main_menu()

  print ('Please enter the option:')
  option = input()

  while option not in ['1', '2', '3', '4', '5']:
    print('Please enter a valid option:')
    show_main_menu()
    option = input()

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

bootstrap()
