import csv
import pandas as pd
from sqlalchemy import create_engine

file = 'cpuo.csv'

df = pd.read_csv(file)

### How many rows are in the DataFrame?
total_rows = df.shape[0]
print("Total rows in the data frame are:",total_rows)

### What columns are included in the DataFrame?
print("The columns in the dataframe are: \n" ,list(df))

### Which NYC police precint received the most complaints in a single year?
df_complaints = df.groupby (['Precinct / Command', 'Year'], as_index=True)['Complaints Count'].sum()
print(df_complaints)
print("NYC police precint received the most complaints:", df_complaints.idxmax())

### What is the average number of complaints against a police precint in a year?
print("The average number of complaints against a police precint in a year?")
print(df_complaints.mean())

### What is the standard deviation from that average?
print("The stdev of the average complaints")
print(df_complaints.std())

### What is the total complaints count, and the total number of officers subject to complaint?
print("Total number of complaints:", df['Complaints Count'].sum())
print("Total number of officers subject to complaints:", df['Number Of Subject Officers'].sum())

### What command, in what year, receieved zero complaints?
print(df.loc[df['Complaints Count'] == 0])

### What is the command to insert your DataFrame into a SQLite database?
engine = create_engine('sqlite://', echo=False)
df_complaints.to_sql('Complaints Count', con=engine)