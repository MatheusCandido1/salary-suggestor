import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

def generate_chart():
    data = pd.read_csv('new_salaries.csv')  
    sns.histplot(data['salary_in_usd'], kde=True, stat="density")
    data[['salary_in_usd']].describe()
    plt.show()

