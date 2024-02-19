class UniversityManagementSystem:
    def _init_(self):
        self.students = {}
        self.courses = {}
        self.enrollments = []

    def add_student(self, student_id, name, age):
        if student_id not in self.students:
            self.students[student_id] = {"name": name, "age": age}
            print(f"Student {name} added to the university.")
        else:
            print("Student ID already exists. Please use a different ID.")

    def remove_student(self, student_id):
        if student_id in self.students:
            del self.students[student_id]
            print("Student removed from the university.")
        else:
            print("Student not found.")

    def display_students(self):
        if not self.students:
            print("No students in the university.")
        else:
            print("Students in the university:")
            for student_id, details in self.students.items():
                print(f"ID: {student_id}, Name: {details['name']}, Age: {details['age']}")

    def add_course(self, course_code, name, credits):
        if course_code not in self.courses:
            self.courses[course_code] = {"name": name, "credits": credits}
            print(f"Course {name} added to the university.")
        else:
            print("Course code already exists. Please use a different code.")

    def remove_course(self, course_code):
        if course_code in self.courses:
            del self.courses[course_code]
            print("Course removed from the university.")
        else:
            print("Course not found.")

    def display_courses(self):
        if not self.courses:
            print("No courses in the university.")
        else:
            print("Courses in the university:")
            for course_code, details in self.courses.items():
                print(f"Code: {course_code}, Name: {details['name']}, Credits: {details['credits']}")

    def enroll_student(self, student_id, course_code):
        if student_id in self.students and course_code in self.courses:
            enrollment = {"student_id": student_id, "course_code": course_code}
            self.enrollments.append(enrollment)
            print(f"Student {self.students[student_id]['name']} enrolled in course {self.courses[course_code]['name']}.")
        else:
            print("Student or course not found.")

    def display_enrollments(self):
        if not self.enrollments:
            print("No enrollments in the university.")
        else:
            print("Enrollments in the university:")
            for enrollment in self.enrollments:
                student_name = self.students[enrollment["student_id"]]["name"]
                course_name = self.courses[enrollment["course_code"]]["name"]
                print(f"Student: {student_name}, Course: {course_name}")


def main():
    university = UniversityManagementSystem()

    while True:
        print("\nUniversity Management System")
        print("1. Add Student")
        print("2. Remove Student")
        print("3. Display Students")
        print("4. Add Course")
        print("5. Remove Course")
        print("6. Display Courses")
        print("7. Enroll Student in Course")
        print("8. Display Enrollments")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            student_id = input("Enter Student ID: ")
            name = input("Enter Name: ")
            age = input("Enter Age: ")
            university.add_student(student_id, name, age)
        elif choice == "2":
            student_id = input("Enter Student ID to remove: ")
            university.remove_student(student_id)
        elif choice == "3":
            university.display_students()
        elif choice == "4":
            course_code = input("Enter Course Code: ")
            name = input("Enter Name: ")
            credits = input("Enter Credits: ")
            university.add_course(course_code, name, credits)
        elif choice == "5":
            course_code = input("Enter Course Code to remove: ")
            university.remove_course(course_code)
        elif choice == "6":
            university.display_courses()
        elif choice == "7":
            student_id = input("Enter Student ID: ")
            course_code = input("Enter Course Code: ")
            university.enroll_student(student_id, course_code)
        elif choice == "8":
            university.display_enrollments()
        elif choice == "9":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")


if __name__ == "_main_":
    main()
