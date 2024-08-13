class AttendanceSystem:
    def __init__(self): # Initialize the AttendanceSystem class with an empty list to store student names and a dictionary to store attendance records.
        
        self.students = []  # List to store student names
        self.attendance = {}  # Dictionary to store attendance records

    def add_student(self, name): # `add_student` method adds a new student to the system.
        
        if name not in self.students:
            self.students.append(name)  # Add the student to the list
            self.attendance[name] = []  # Initialize attendance record for the student
            print(f"Student '{name}' added successfully.")
        else:
            print(f"Student '{name}' is already in the system.")

    def mark_attendance(self): # `mark_attendance` method allows marking attendance for students.
        
        print("\nMark Attendance") # Prompt the user to enter attendance status for each student
        for student in self.students:
            status = input(f"Is {student} present? (yes/no): ").strip().lower()
            if status == 'yes':
                self.attendance[student].append('Present')  # Mark as present
            else:
                self.attendance[student].append('Absent')  # Mark as absent
        print("Attendance marked successfully.")

    def view_attendance(self): # Allows to view the attendance records for all students.
        
        print("\nAttendance Records:")
        for student, records in self.attendance.items():
            print(f"{student}: {', '.join(records)}")  # Print each student's attendance

def main():# The main function is the entry point of the program.
    
    attendance_system = AttendanceSystem()  # Create an instance of the AttendanceSystem


    while True: # The program enters a loop that allows the user to perform various actions.
        print("\nVirtual Classroom Attendance System")
        print("1. Add Student")
        print("2. Mark Attendance")
        print("3. View Attendance Records")
        print("4. Exit")


        choice = input("Choose an option: ")


        if choice == '1':
            student_name = input("Enter the student's name: ")
            attendance_system.add_student(student_name)  # Add a new student


        elif choice == '2':
            attendance_system.mark_attendance()  # Mark attendance for students


        elif choice == '3':
            attendance_system.view_attendance()  # View attendance records


        elif choice == '4':
            print("Exiting the Attendance System. Goodbye!")
            break  # Exit the loop


        else:
            print("Invalid option. Please choose again.")


if __name__ == "__main__":
    main()  # Run the main function
