students = {}
# Function to add a new student
def add_student(student_id, name):
    if student_id in students:
        print("Student ID already exists.")
    else:
        students[student_id] = {'name': name, 'grades': [], 'attendance': 0}
        print(f"Student {name} added successfully!")

# Function to update grades
def update_grades(student_id, grade):
    if student_id in students:
        students[student_id]['grades'].append(grade)
        print(f"Grade {grade} added for {students[student_id]['name']}.")
    else:
        print("Student not found.")

# Function to update attendance
def update_attendance(student_id):
    if student_id in students:
        students[student_id]['attendance'] += 1
        print(f"Attendance updated for {students[student_id]['name']}.")
    else:
        print("Student not found.")

# Function to display student records
def display_students():
    if not students:
        print("No student records available.")
    else:
        for student_id, details in students.items():
            print(f"ID: {student_id}, Name: {details['name']}, Grades: {details['grades']}, Attendance: {details['attendance']} days")

# Function to calculate the average grade of a student
def calculate_average(student_id):
    if student_id in students:
        grades = students[student_id]['grades']
        if grades:
            avg = sum(grades) / len(grades)
            print(f"Average grade for {students[student_id]['name']}: {avg:.2f}")
        else:
            print("No grades available.")
    else:
        print("Student not found.")

# Sample Usage
add_student(1, "SEEMA")
add_student(2, "RAM")

update_grades(1, 85)
update_grades(1, 90)
update_grades(2, 78)

update_attendance(1)
update_attendance(2)
update_attendance(1)

display_students()
calculate_average(1)

