import MySQLdb

# Replace these with your actual MySQL connection details
host = 'localhost'
user = 'root'
password = 'Pandhurna@21'
database = 'world'

try:
    conn = MySQLdb.connect(host="localhost", user="root", passwd="Pandhurna@21", db="world")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM country")
    rows = cursor.fetchall()
    print(len(rows))
    print("Connection established")
except:
    print(f"Error")

