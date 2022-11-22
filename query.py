import pyodbc
import pandas as pd

conx_string = "DRIVER= {SQL SERVER} ; SERVER=DESKTOP-1VFJKRB\SQLEXPRESS; database=UC2_DHSANG; trusted_connection=YES;" #TODO:run driver.py to check
query = "SELECT * FROM UC2_DHSANG.dbo.products"

conx = pyodbc.connect(conx_string)
cursor = conx.cursor()

cursor.execute(query)

data = cursor.fetchall()

print(data)
print(type(data))

df = pd.DataFrame()

idx = []
name = []
cost = []

for i in range(len(data)):
    idx.append(data[i][0])
    name.append(data[i][1])
    cost.append(data[i][2])

df["index"] = idx
df["name"] = name
df["cost"] = cost

df.to_csv("table.csv")

conx.close()
