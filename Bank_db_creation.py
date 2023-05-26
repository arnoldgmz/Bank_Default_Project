import pandas as pd
import numpy as np
import random
from sqlalchemy import create_engine
from faker import Faker


# instance the faker class
fake = Faker()

# Define the possible categorios for job type and marital status
job_types = ['Engineer', 'Doctor', 'Teacher', 'Chef', 'Driver',
             'Designer', 'Developer', 'Manager', 'Clerk', 'Other']
maritual_status = ['Single', 'Married', 'Divorced', 'Widowed']

# Generate Data

data = {
    'Age': np.random.randint(20, 70, size=10000),
    'Income': np.random. randint(30000, 150000, size=10000),
    'Loan Amount': np.random.randint(50000, 500000, size=10000),
    'Credit Score': np.random.randint(300, 850, size=10000),
    'Job Type': [random.choice(job_types) for _ in range(10000)],
    'Marital Status': [random.choice(maritual_status) for _ in range(10000)],
    'Default': [random.choice(['Yes', 'No']) for _ in range(10000)],
}

# Create a dataframe
df = pd.DataFrame(data)

# Print the dataframe
print(df)

# create an SQL databse
engine = create_engine('sqlite:///my_databse.db')

# write the DataFrame to a table in the SQL Database
df.to_sql('df', engine, if_exists='replace', index=False)
