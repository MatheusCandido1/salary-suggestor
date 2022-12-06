import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

data = pd.read_csv('new_salaries.csv')


def format_currency(value):
  return '${:,.2f}'.format(value)

def generate_statistics():
    print('\nStatistics \n')
    print('-----------------------------------')
    print('Mean: '.ljust(20), format_currency(data['salary_in_usd'].mean()))
    print('Median: '.ljust(20), format_currency(data['salary_in_usd'].median()))
    print('Standart Deviation: '.ljust(20), format_currency(data['salary_in_usd'].std()))
    print('Maximum Salary: '.ljust(20), format_currency(data['salary_in_usd'].max()))
    print('Minimum Salary: '.ljust(20), format_currency(data['salary_in_usd'].min()))
    print('25th Percentile: '.ljust(20), format_currency(data['salary_in_usd'].quantile(0.25)))
    print('50th Percentile: '.ljust(20), format_currency(data['salary_in_usd'].quantile(0.5)))
    print('75th Percentile: '.ljust(20), format_currency(data['salary_in_usd'].quantile(0.75)))
    print('-----------------------------------')

def generate_chart():
    sns.histplot(data['salary_in_usd'], kde=True, stat="density")
    data[['salary_in_usd']].describe()
    plt.show()

