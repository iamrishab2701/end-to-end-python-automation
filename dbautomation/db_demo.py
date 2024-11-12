import mysql.connector

from utilities.configurations import get_mysql_connection

# Parameters - host, database name, authentication
# mysql_connection = mysql.connector.connect(host='localhost',
#                                            database='APIDevelop',
#                                            user='root',
#                                            password='RSmay2024')

mysql_connection = get_mysql_connection()
print(mysql_connection.is_connected())

# To query we can use cursor object
mysql_cursor = mysql_connection.cursor()
mysql_cursor.execute("select * from CustomerInfo")
row = mysql_cursor.fetchone()  # Tuples
print(row)
print(row[3])
row_all = mysql_cursor.fetchall()  # List of Tuples
print(row_all)
print(row_all[1])

# Sum of all the amount
total_amount = 0
for row in row_all:
    total_amount += row[2]
print(total_amount)
assert total_amount == 765

# CRUD operation
# Updating the data
update_query = "update customerInfo set Location = %s where CourseName = %s"
update_data = ("US", "Jmeter")
mysql_cursor.execute(update_query, update_data)

# Commiting the changes after executing.
mysql_connection.commit()

# Deleting the data
delete_query = "delete from CustomerInfo where courseName = 'Protractor'"
mysql_cursor.execute(delete_query)
mysql_connection.commit()

# Closing the connection
mysql_cursor.close()
