import mysql.connector

print("Starting pure Python MySQL test...", flush=True)

try:
    connection = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        database="registration_db",
        user="registration_user",
        password="registration_password",
        connection_timeout=10,
        use_pure=True
    )

    print("MYSQL CONNECTION SUCCESSFUL", flush=True)

    cursor = connection.cursor()
    cursor.execute("SELECT 1")

    print("QUERY RESULT:", cursor.fetchone(), flush=True)

    cursor.close()
    connection.close()

    print("TEST COMPLETED SUCCESSFULLY", flush=True)

except Exception as e:
    print("MYSQL ERROR:", type(e).__name__, flush=True)
    print(e, flush=True)
    sys.exit(1)