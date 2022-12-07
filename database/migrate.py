"""
* Author: Matheus Carvalho, Amber Upton, Fatima Gonzales, Javier Segura, Sweastik Pokhrel
* Date: 12-06-2022
"""
# Import tables, init, seeds from other files
import tables, init, seeds

# Run the create_database function inside the file init.py
init.use_database()

# Run the create_tables function inside the file tables.py
tables.create_tables()

# Run the companies_seeder function inside the file seeds.py
seeds.seed()

