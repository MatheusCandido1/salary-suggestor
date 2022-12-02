"""
* Author: Matheus Carvalho
* Date: 09-28-2022
"""

from controllers import company_controller

def update_company(company):
  print('Current Name: '+ str(company[0][1]))
  name = input('New Name: ')

  while name == '':
    name = input('New Name: ')

  print('Current Address: '+ str(company[0][2]))
  address = input('New Address: ')

  while address == '':
    address = input('New Address: ')

  updateCompany = {
    'id': company[0][0],
    'name': name,
    'address': address,
  }
  
  company_controller.update(updateCompany)



def welcome(company):
  print('\nThis software belongs to ' + str(company[0][1]) + '\n')

  print('Company Information:')
  print('Name: ' + str(company[0][1]))
  print('Address: ' + str(company[0][2]))

def show_menu():
  print('\nMenu: \n')

  print('1 - Manage Company')
  print('2 - Manage Candidates')
  print('3 - Manage Proposals')
  print('4 - Exit \n')


company = company_controller.index()
welcome(company)

print('Would you like to update any information about the company? (y/n)')
answer = input()

if answer.lower() == 'y':
  update_company(company)

show_menu()

option = input()

while option != '4':
  print('Software runs here')

  option = input()

if option == '4':
  print('Thank you for using our software!')
  exit()


