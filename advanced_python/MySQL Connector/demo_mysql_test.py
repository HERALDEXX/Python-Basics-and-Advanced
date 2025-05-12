'''Note: This code is cellular and should be run in a compatible environment that supports Jupyter notebooks or similar interfaces.'''
'''This code is for demonstration purposes only and may require a MySQL server running locally or remotely.'''

# %%
'''Import necessary libraries'''
import os
import mysql.connector

# %%
'''Load environment variables from your .env file (Optional)'''
from dotenv import load_dotenv
load_dotenv()

# %%
'''Connect to MySQL database'''
# Note: Hardcode the connection parameters for simplicity 
# or Ensure that the .env file contains MYSQL_HOST, MYSQL_USER, and MYSQL_PASSWORD variables
mydb = mysql.connector.connect(
  host=os.getenv("MYSQL_HOST"),
  user=os.getenv("MYSQL_USER"),
  password=os.getenv("MYSQL_PASSWORD"),
  database=os.getenv("MYSQL_DATABASE")
)

'''Verify MySQL database connection'''
print("Connected to MySQL database")
print(mydb)


# %%
mycursor = mydb.cursor()

'''Check existing databases'''
print("Existing databases:")
mycursor.execute("SHOW DATABASES")
for db in mycursor:
    print(db)


# %%
'''Create a new database'''
mycursor.execute("CREATE DATABASE test_db")


# %%
'''Create MySQL table in Python'''
# Check existing tables
mycursor.execute("SHOW TABLES")
for table in mycursor:
    print(table)


# %%
'''Create a new table'''
mycursor.execute("CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), email VARCHAR(255))")    


# %%
'''Add a new column to the existing table'''
mycursor.execute("ALTER TABLE users ADD COLUMN age INT")  # Add age column to users table


# %%
'''Insert data into the table'''
# Note: Ensure that the table 'users' exists before running this code
sql = "INSERT INTO users (name, email, age) VALUES (%s, %s, %s)"
val = ("Herald Inyang", "herald@example.com", 18)

mydb.commit()  # Commit the transaction
mycursor.execute(sql, val)
print(mycursor.rowcount, "record inserted.")


# %%
'''Entering multiple values'''
sql = "INSERT INTO users (name, email, age) VALUES (%s, %s, %s)"
val = [
    ("Adesua Ayomitan", "adesua@example.com", 20), 
    ("Jane Doe", "jane@example.com", 25)
    ]

mydb.commit()  # Commit the transaction
mycursor.executemany(sql, val)
print(mycursor.rowcount, "record inserted.")


# %%
'''Insert a single record and retrieve the last inserted ID'''
print("1 record inserted, ID:", mycursor.lastrowid)


# %%
'''Retrieve data from the table'''
mycursor.execute("SELECT * FROM users")
result = mycursor.fetchall()
for row in result:
    print(row)


# %%
'''Retrieve filtered data from the table'''
mycursor.execute("SELECT * FROM users WHERE age > 20")
result = mycursor.fetchall()
for row in result:
    print(row)


# %%
'''Close the cursor and database connection'''
mycursor.close()
mydb.close()