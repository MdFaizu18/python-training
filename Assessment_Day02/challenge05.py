# Sort dictionary by marks

students = {"Faizu": 78, "Hari": 90, "vinitha": 65}
ranked = sorted(students.items(), key=lambda x: x[1], reverse=True)
print(ranked)