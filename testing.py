# test_connection_strings.py
import psycopg2
from psycopg2 import OperationalError

def test_connection(conn_string, description):
    print(f"\nTesting: {description}")
    print(f"Connection string: {conn_string}")
    
    try:
        connection = psycopg2.connect(conn_string)
        cursor = connection.cursor()
        cursor.execute("SELECT current_database();")
        db_name = cursor.fetchone()
        print(f"✅ SUCCESS: Connected to {db_name[0]}")
        cursor.close()
        connection.close()
        return True
    except OperationalError as e:
        print(f"❌ FAILED: {e}")
        return False

# Test different connection string formats
test_cases = [
    ("dbname=agno_db user=postgres password=pheo259f host=localhost port=5432", "Parameter string"),
    ("postgresql://postgres:pheo259f@localhost:5432/agno_db", "URL format"),
    ("postgresql://postgres:pheo259f@127.0.0.1:5432/agno_db", "URL with 127.0.0.1"),
    ("host=localhost dbname=agno_db user=postgres password=pheo259f", "Alternative parameter order"),
]

all_success = True
for conn_string, description in test_cases:
    if not test_connection(conn_string, description):
        all_success = False

if all_success:
    print("\n🎉 All connection tests passed!")
else:
    print("\n🔧 Some connection tests failed.")