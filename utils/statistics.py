# Import Pandas
import pandas as pd
# Import Matplotlib
import matplotlib.pyplot as plt
# Import Seaborn
import seaborn as sns

# Read the CSV file
data = pd.read_csv('new_salaries.csv')

# Define function to format currency
def format_currency(value):
  return '${:,.2f}'.format(value)

# Define function to generate statistics
def generate_statistics():
  # Print the statistics
  print('\nStatistics \n')
  print('-----------------------------------')
  # Print the Mean
  print('Mean: '.ljust(20), format_currency(data['salary_in_usd'].mean()))
  # Print the Median
  print('Median: '.ljust(20), format_currency(data['salary_in_usd'].median()))
  # Print the Standard Deviation
  print('Standard Deviation: '.ljust(20), format_currency(data['salary_in_usd'].std()))
  # Print the Maximum Salary
  print('Maximum Salary: '.ljust(20), format_currency(data['salary_in_usd'].max()))
  # Print the Minimum Salary
  print('Minimum Salary: '.ljust(20), format_currency(data['salary_in_usd'].min()))
  # Print the 25th, 50th, and 75th Percentiles
  print('25th Percentile: '.ljust(20), format_currency(data['salary_in_usd'].quantile(0.25)))
  print('50th Percentile: '.ljust(20), format_currency(data['salary_in_usd'].quantile(0.5)))
  print('75th Percentile: '.ljust(20), format_currency(data['salary_in_usd'].quantile(0.75)))
  print('-----------------------------------')

# Define function to generate the chart
def generate_chart():
  # Create a figure using the data
  sns.histplot(data['salary_in_usd'], kde=True, stat="density")
  data[['salary_in_usd']].describe()
  # Show the plot
  plt.show()

