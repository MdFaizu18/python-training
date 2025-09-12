from datetime import datetime
from db_config import get_connection

# To add the new employee 
def add_employee(name,department):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO employees (name,department) VALUES (%s,%s)",(name,department))
        conn.commit()
        return True
    except Exception as e:
        print(f"Error adding employee: {e}")
        return False
    finally:
        cursor.close()
        conn.close()
        
# Employee check-in
def check_in(employee_id):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM attendance WHERE employee_id=%s AND check_out IS NULL",(employee_id,))
        if cursor.fetchone():
            print("Employee already checked in.")
            return False
        cursor.execute("INSERT INTO attendance (employee_id,check_in) VALUES (%s,%s)",(employee_id,datetime.now()))
        conn.commit()
        return True
    except Exception as e:
        print(f"Error during check-in: {e}")
        return False
    finally:
        cursor.close()
        conn.close()
        
# Employee check-out
def check_out(employee_id):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM attendance WHERE employee_id=%s AND check_out IS NULL",(employee_id,))
        if not cursor.fetchone():
            print("Employee not checked in.")
            return False
        cursor.execute("UPDATE attendance SET check_out=%s WHERE employee_id=%s AND check_out IS NULL",(datetime.now(),employee_id))
        conn.commit()
        return True
    except Exception as e:
        print(f"Error during check-out: {e}")
        return False
    finally:
        cursor.close()
        conn.close()
        
# View report records
def generate_report(employee_id):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        query = """
        SELECT e.name, e.department, a.check_in, a.check_out, a.total_hours
        FROM attendance a
        JOIN employees e ON a.employee_id = e.employee_id
        WHERE e.employee_id = %s
        """
        cursor.execute(query, (employee_id,))
        rows = cursor.fetchall()

        for row in rows:
            print(row)

    except Exception as e:
        print("Error:", e)
    finally:
        conn.close()


# List employees with incomplete attendance
def list_incomplete():
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
        SELECT e.name, e.department, a.check_in
        FROM attendance a
        JOIN employees e ON a.employee_id = e.employee_id
        WHERE a.check_out IS NULL
        """)
        return cursor.fetchall()
    except Exception as e:
        print("Error:", e)
        return []
    finally:
        conn.close()