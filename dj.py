import pyodbc

# Define your connection parameters
# server = 'localhost'  # Replace with your SQL Server hostname or IP address
server = '190.2.133.223'  # Replace with your SQL Server hostname or IP address
database = 'pressPilot'  # Replace with your database name
username = 'pressPilot'  # Replace with your username
# password = 'Topikinos2001'  # Replace with your password
password = '1234'  # Replace with your password
port = '1638'  # Replace with the SQL Server port you're using

# Connection string
# connection_string = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={server},{port};DATABASE={database};UID={username};PWD={password}'
connection_string = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={server},{port};DATABASE={database};UID={username};PWD={password};TrustServerCertificate=Yes'


try:
    # Establish the connection
    conn = pyodbc.connect(connection_string)

    # Create a cursor
    cursor = conn.cursor()

    # Execute a simple query to test the connection
    cursor.execute('SELECT 1')

    # Fetch and print the result
    result = cursor.fetchone()
    print("Connection successful. Result:", result[0])

    # Clean up
    cursor.close()
    conn.close()

except Exception as e:
    print("Connection failed. Error:", str(e))
