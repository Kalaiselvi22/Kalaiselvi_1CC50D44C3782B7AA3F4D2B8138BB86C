class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

def sort_students(student_list):
    sorted_students = sorted(student_list, key=lambda x: x.cgpa, reverse=True)
    return sorted_students

# Test the function with different input lists of students
if __name__ == "__main__":
    # Create a list of student objects
    students = [
        Student("Alice", "A001", 3.8),
        Student("Bob", "B002", 3.6),
        Student("Charlie", "C003", 3.9),
        Student("David", "D004", 3.7),
    ]

    # Sort the students by CGPA in descending order
    sorted_students = sort_students(students)

    # Print the sorted list of students
    for student in sorted_students:
        print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")
