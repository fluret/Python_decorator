@retry_on_failure(max_retries=3, delay=2)
def connect_to_database():
    conn = sqlite3.connect("example.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

try:
    data = connect_to_database()
    print("Data retrieved successfully:", data)
except Exception as e:
    print(f"Failed to connect to the database: {e}")
