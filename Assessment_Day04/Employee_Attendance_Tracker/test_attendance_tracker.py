import inspect
import pytest
from attendance_functions import AttendanceDB   # your class file

# ---------------- QUERY TESTS ---------------- #

def test_add_employee_query():
    db = AttendanceDB()
    expected = "INSERT INTO employees (name, department) VALUES (%s, %s)"
    actual = inspect.getsource(db.add_employee)
    assert expected in actual

def test_check_in_query():
    db = AttendanceDB()
    expected = "INSERT INTO attendance (employee_id, checkin_time) VALUES (%s, NOW())"
    actual = inspect.getsource(db.check_in)
    assert expected in actual

def test_check_out_query():
    db = AttendanceDB()
    expected = "UPDATE attendance SET checkout_time = NOW() WHERE employee_id = %s AND checkout_time IS NULL"
    actual = inspect.getsource(db.check_out)
    assert expected in actual

def test_generate_report_query():
    db = AttendanceDB()
    expected = "SELECT * FROM attendance WHERE employee_id = %s"
    actual = inspect.getsource(db.generate_report)
    assert expected in actual

def test_list_incomplete_query():
    db = AttendanceDB()
    expected = "SELECT * FROM attendance WHERE checkout_time IS NULL"
    actual = inspect.getsource(db.list_incomplete)
    assert expected in actual


def test_add_employee():
    sig = inspect.signature(AttendanceDB.add_employee)
    assert list(sig.parameters.keys()) == ["self", "name", "department"]

def test_check_in():
    sig = inspect.signature(AttendanceDB.check_in)
    assert list(sig.parameters.keys()) == ["self", "employee_id"]

def test_check_out():
    sig = inspect.signature(AttendanceDB.check_out)
    assert list(sig.parameters.keys()) == ["self", "employee_id"]

def test_generate_report():
    sig = inspect.signature(AttendanceDB.generate_report)
    assert list(sig.parameters.keys()) == ["self", "employee_id"]

def test_list_incomplete():
    sig = inspect.signature(AttendanceDB.list_incomplete)
    assert list(sig.parameters.keys()) == ["self"]
