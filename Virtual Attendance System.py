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

