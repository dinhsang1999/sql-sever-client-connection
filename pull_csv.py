import pandas as pd
import pyodbc

conx_string = "DRIVER= {SQL SERVER} ; SERVER=DESKTOP-1VFJKRB\SQLEXPRESS; database=UC2_DHSANG; trusted_connection=YES;" #TODO:run driver.py to check


conx = pyodbc.connect(conx_string)
cursor = conx.cursor()

data = pd.read_csv("example_survey.csv")   
df = pd.DataFrame(data)
# Create Table
cursor.execute('''
		CREATE TABLE surveys_2 (
			year int primary key,
			variable_name nvarchar(100),
			price nvarchar(20),
			)
               ''')

# Insert DataFrame to Table
for row in df.itertuples():
    cursor.execute('''
                INSERT INTO surveys_2 (year, variable_name, price)
                VALUES (?,?,?)
                ''',
                row.Year, 
                row.Variable_name,
                row.Value
                )

conx.commit()