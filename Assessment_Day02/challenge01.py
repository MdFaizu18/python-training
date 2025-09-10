# Sort by second element

employees = [("Faizu", 85), ("Hari", 92), ("Vinitha", 78)]
sorted_employees = sorted(employees, key=lambda x: x[1], reverse=True)
print(sorted_employees)