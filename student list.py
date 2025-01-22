# List to store student records
students = []

# Function to add a student
def add_student():
    name = input("Enter student's name: ")
    student_id = input("Enter student's ID: ")
    grade = input("Enter student's grade: ")
  
    
    student = {
        "name": name,
        "id": student_id,
        "grade": grade,
        
    }
    students.append(student)
    print(f"Student {name} added successfully!")

# Function to view all students
def view_students():
    if not students:
        print("No student records found.")
        return
    print("\n--- Student List ---")
    for idx, student in enumerate(students, start=1):
        print(f"{idx}. Name: {student['name']}, ID: {student['id']}, Grade: {student['grade']}")

# Function to update a student's details
def update_student():
    student_id = input("Enter the ID of the student to update: ")
    for student in students:
        if student["id"] == student_id:
            print("Student found. Update the details below (press Enter to keep current value):")
            new_name = input(f"Current Name: {student['name']}, New Name: ") or student["name"]
            new_grade = input(f"Current Grade: {student['grade']}, New Grade: ") or student["grade"]
            
            
            # Update the student record
            student["name"] = new_name
            student["grade"] = new_grade
           
            print("Student details updated successfully!")
            return
    print("Student with the specified ID not found.")

# Function to delete a student record
def delete_student():
    student_id = input("Enter the ID of the student to delete: ")
    global students
    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            print("Student record deleted successfully!")
            return
    print("Student with the specified ID not found.")

# Menu interface
def menu():
    while True:
        print("\n--- Student Management System ---")
        print("1. Add a Student")
        print("2. View All Students")
        print("3. Update a Student's Details")
        print("4. Delete a Student Record")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Entry point
if __name__ == "__main__":
    menu()
