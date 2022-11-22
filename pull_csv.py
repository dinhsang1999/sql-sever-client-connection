import pandas as pd
import pyodbc

# def connection_string(driver,server_name,database_name):
#     conn_string = f"""
#     DRIVER = {{driver}};
#     SERVER = {server_name};
#     DATABASE = {database_name};
#     TRUST_CONNECTION = yes;
#     """
#     return conn_string
    
conx_string = "DRIVER= {SQL SERVER} ; SERVER=DESKTOP-1VFJKRB\SQLEXPRESS; database=UC2_DHSANG; trusted_connection=YES;" #TODO:run driver.py to check

try:
    conx = pyodbc.connect(conx_string)
except pyodbc.DatabaseError as e:
    print('Database Error:',e)
except pyodbc.Error as e:
    print('Conenction Error:')
    print(str(e.value[1]))

try:
    cursor = conx.cursor()
except Exception as e:
    print(str(e[1]))



data = pd.read_csv("example_survey.csv")   
df = pd.DataFrame(data)
columns = ['Year', 'Industry_aggregation_NZSIOC', 'Industry_code_NZSIOC',    
       'Industry_name_NZSIOC', 'Units', 'Variable_code', 'Variable_name',
       'Variable_category', 'Value', 'Industry_code_ANZSIC06']
df_data = df[columns]
# Create Table
# Creating a table called surveys with the columns listed.
cursor.execute("CREATE TABLE survey (YEAR int,NAME nvarchar(100),VALUE nvarchar(100))")

# Insert DataFrame to Table
for row in df.itertuples():
    cursor.execute('''
                INSERT INTO survey (YEAR, NAME, VALUE)
                VALUES (?,?,?)
                ''',
                row.Year, 
                row.Variable_name,
                row.Value
                )

conx.commit()