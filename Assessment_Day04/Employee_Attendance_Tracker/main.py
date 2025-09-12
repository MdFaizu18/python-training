from attendance_functions import add_employee, check_in, check_out, generate_report, list_incomplete

def main():
    while True:
        print("\n===== Employee Attendance Tracker =====")
        print("1. Add New Employee")
        print("2. Employee Check-in")
        print("3. Employee Check-out")
        print("4. Generate Report")
        print("5. List Incomplete Attendance")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter employee name: ")
            dept = input("Enter department: ")
            if add_employee(name, dept):
                print("Employee added successfully!")
            else:
                print(" Failed to add employee.")

        elif choice == "2":
            emp_id = int(input("Enter employee ID: "))
            print(check_in(emp_id))

        elif choice == "3":
            emp_id = int(input("Enter employee ID: "))
            print(check_out(emp_id))

        elif choice == "4":
            emp_id = int(input("Enter employee ID: "))
            print("\nAttendance Report:")
            records = generate_report(emp_id)
            for rec in records:
                print(rec)

        elif choice == "5":
            print("\n Employees with incomplete attendance:")
            rows = list_incomplete()
            for row in rows:
                print(row)

        elif choice == "6":
            print(" Exiting... Goodbye!")
            break

        else:
            print(" Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
