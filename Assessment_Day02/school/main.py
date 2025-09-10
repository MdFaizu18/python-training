import student, teacher, results

student.add_student("Faizu")
teacher.subject_allocation("Karthik", "Maths")
print("Students:", student.list_students())
print("Teachers:", teacher.view_teachers())
print("Grade:", results.grade_calculation(82))
