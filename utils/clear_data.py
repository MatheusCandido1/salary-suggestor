import numpy as np # importing numpy and pandas
import pandas as pd

#read csv file
completeData = pd.read_csv("salaries.csv")

#drop unnecessary columns
completeData = completeData.drop('index', axis=1) # get rid of index
completeData = completeData.drop('remote_ratio', axis=1)
completeData = completeData.drop('work_year', axis=1)
completeData = completeData.drop('job_title', axis=1)
completeData = completeData.drop('company_location', axis=1)

#check number of US resident entries so that when we get rid of everything, we know how many we should have
numUsData = completeData['employee_residence'].value_counts()['US'] #332 entries for US residents
usData = completeData.loc[completeData['employee_residence'] == 'US'] #has 332 rows yay

#get rid of columns you do not need after using only US data
usData= usData.drop('salary_currency', axis=1)
usData= usData.drop('salary', axis=1)
usData=usData.drop('employee_residence', axis=1)


#make new columns for different company size: Small, Medium and Large and converting them into zero and ones
usData['Medium companies'] = usData.loc[:, 'company_size']
# converting median companies M =1 everything else = 0
usData.loc[usData['Medium companies'] != 'M', 'Medium companies'] = 0
usData.loc[usData['Medium companies'] == 'M', 'Medium companies'] = 1

usData['Small companies'] = usData.loc[:, 'company_size']
# converting Small companies S =1 everything else = 0
usData.loc[usData['Small companies'] != 'S', 'Small companies'] = 0
usData.loc[usData['Small companies'] == 'S', 'Small companies'] = 1

usData['Large companies'] = usData.loc[:, 'company_size']
# converting Small companies S =1 everything else = 0
usData.loc[usData['Large companies'] != 'L', 'Large companies'] = 0
usData.loc[usData['Large companies'] == 'L', 'Large companies'] = 1
#dropping company size from table
usData = usData.drop('company_size', axis=1)

# make new columns for differnet employee types: Full Time, Part Time, Contract and Freelance
usData['Full Time'] = usData.loc[:, 'employment_type']
#Converting values to zero and ones FT =1 everything else = 0
usData.loc[usData['Full Time'] != 'FT', 'Full Time'] = 0
usData.loc[usData['Full Time'] == 'FT', 'Full Time'] = 1

usData['Part Time'] = usData.loc[:, 'employment_type']
#Converting values to zero and ones PT =1 everything else = 0
usData.loc[usData['Part Time'] != 'PT', 'Part Time'] = 0
usData.loc[usData['Part Time'] == 'PT', 'Part Time'] = 1

usData['Contract'] = usData.loc[:, 'employment_type']
#Converting values to zero and ones CT =1 everything else = 0
usData.loc[usData['Contract'] != 'CT', 'Contract'] = 0
usData.loc[usData['Contract'] == 'CT', 'Contract'] = 1

usData['Freelance'] = usData.loc[:, 'employment_type']
#Converting values to zero and ones FL =1 everything else = 0
usData.loc[usData['Freelance'] != 'FL', 'Freelance'] = 0
usData.loc[usData['Freelance'] == 'FL', 'Freelance'] = 1

#make mew columns for differnet experiance levels: Entry level, Mid level, Senior Level and Executive Level
usData['Entry level'] = usData.loc[:, 'experience_level']
#Converting values to zeros and ones EN = 1 everything else =0
usData.loc[usData['Entry level'] != 'EN', 'Entry level'] = 0
usData.loc[usData['Entry level'] == 'EN', 'Entry level'] = 1

usData['Mid level'] = usData.loc[:, 'experience_level']
#Converting values to zeros and ones MI = 1 everything else =0
usData.loc[usData['Mid level'] != 'MI', 'Mid level'] = 0
usData.loc[usData['Mid level'] == 'MI', 'Mid level'] = 1

usData['Senior Level'] = usData.loc[:, 'experience_level']
#Converting values to zeros and ones SE = 1 everything else =0
usData.loc[usData['Senior Level'] != 'SE', 'Senior Level'] = 0
usData.loc[usData['Senior Level'] == 'SE', 'Senior Level'] = 1

usData['Executive Level'] = usData.loc[:, 'experience_level']
#Converting values to zeros and ones EX = 1 everything else =0
usData.loc[usData['Executive Level'] != 'EX', 'Executive Level'] = 0
usData.loc[usData['Executive Level'] == 'EX', 'Executive Level'] = 1
#getting rid of Experince level, employment type
usData=usData.drop('experience_level', axis=1)
usData=usData.drop('employment_type', axis=1)
usData   
#writing new csv file
print('Writing new csv file')
usData.to_csv('new_salaries.csv')
print('New file named new_salaries.csv was created successfully')
