import pyodbc

### Use the pyodbc.drivers() method to find available drivers; 
# the connection strings for these are essentially the same and will look like this:
# conx = pyodbc.connect('DRIVER={SQL Server}; SERVER=TestServer; Database=TestDatabase; UID=UserID; PWD=Password;')

### If you use Windows Authentication to connect to the server, your string will look like this:
conx_string = "DRIVER= {SQL SERVER} ; SERVER=DESKTOP-1VFJKRB\SQLEXPRESS; database=UC2_DHSANG; trusted_connection=YES;" #TODO:run driver.py to check

####-----------------CONNECT AND EXTRACT DATA--------------#
#Connect
conx = pyodbc.connect(conx_string)

#Create cursor
cursor = conx.cursor()

#Create new table
cursor.execute('''
		INSERT INTO products (product_id, product_name, price)
		VALUES
			(1,'Desktop Computer',800),
			(2,'Laptop',1200),
			(3,'Tablet',200),
			(4,'Monitor',350),
			(5,'Printer',150)
                ''')
conx.commit()