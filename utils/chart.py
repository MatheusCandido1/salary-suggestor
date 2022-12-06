import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def generate_chart():
    data = pd.read_csv('new_salaries.csv')  
    sns.distplot(data['salary_in_usd']).set_title('Data Scientist Salaries - US')
    data[['salary_in_usd']].describe()
    plt.show()

