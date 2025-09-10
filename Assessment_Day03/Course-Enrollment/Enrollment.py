class Enrollment:
    def __init__(self):
        self.courses = []
        self.last_enrolled_course = None  # dynamic attribute

    def enroll_course(self, course):
        if course not in self.courses:
            self.courses.append(course)
            self.last_enrolled_course = course.name
            print(f"Enrolled '{course.name}'.")
        else:
            print(f"Already enrolled in '{course.name}'.")

    def drop_course(self, course):
        if course in self.courses:
            self.courses.remove(course)
            print(f"Dropped '{course.name}'.")
        else:
            print(f"Course '{course.name}' not found in enrollment.")

    def calculate_credits(self):
        return sum(course.credits for course in self.courses)

    def calculate_fees(self):
        return sum(course.get_fee() for course in self.courses)

    def view_enrollment(self):
        if not self.courses:
            print("No courses enrolled yet.")
        else:
            print("Enrolled Courses:")
            for c in self.courses:
                print(f"- {c.display()}")
