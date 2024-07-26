# this whole slide will be enhancing my file handling skills
# starting with Text files
# MENU DRIVEN PROGRAM FOR TEXT FILE
class Student:
    def __init__(self, name, student_class, roll_no):
        self.name = name
        self.student_class = student_class
        self.roll_no = roll_no

    def __str__(self):
        return f"{self.name} is a student of Class {self.student_class} assigned Roll No: {self.roll_no}"

def write():
    """Function to write student record to file."""
    with open("textfile.txt", "w") as file:
        name = input("Enter Name of Student: ")
        student_class = input("Enter Class of Student: ")
        roll_no = input("Enter the Roll No. Student: ")
        student = Student(name, student_class, roll_no)
        file.write(str(student) + "\n")

def append():
    """Function to append new student record to file."""
    with open("textfile.txt", 'a') as file:
        while True:
            print("\nNew Record for addition (Enter 'close' to stop):")
            name = input("Enter Name of Student: ")
            if name.lower() == "close":
                break
            student_class = input("Enter Class of Student: ")
            roll_no = input("Enter the Roll No. Student: ")
            student = Student(name, student_class, roll_no)
            file.write(str(student) + "\n")

def read():
    """Function to read student records from file."""
    with open("textfile.txt", 'r') as file:
        for line in file:
            print(line.strip())

def search():
    """Function to search for a student record in file by roll number."""
    roll_no = input("Enter the Roll No. of student for searching: ")
    found = False
    with open("textfile.txt", "r") as file:
        for line in file:
            if roll_no in line:
                print(line.strip())
                found = True
    if not found:
        print("Search not found.")

def update():
    """Function to update a student record in file by roll number."""
    roll_no = input("Enter the Roll No. of student to update: ")
    updated = False
    with open('textfile.txt', "r+") as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            if roll_no in line:
                print(f"Found record: {line.strip()}")
                name = input("Enter the updated name: ")
                student_class = input("Enter the updated class: ")
                roll_no = input("Enter the updated Roll no.: ")
                updated_student = Student(name, student_class, roll_no)
                file.write(str(updated_student) + "\n")
                updated = True
            else:
                file.write(line)
        file.truncate()
    if not updated:
        print("Student record not found.")

def delete():
    """Function to delete a student record from file by roll number and class."""
    roll_no = input("Enter Roll No. Of Student to delete: ")
    student_class = input("Enter Class of student: ")
    deleted = False
    with open("textfile.txt", "r+") as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            if f"Class {student_class} assigned Roll No: {roll_no}" not in line:
                file.write(line)
            else:
                deleted = True
        file.truncate()
    if deleted:
        print(f"Record with Roll No {roll_no} and Class {student_class} deleted.")
    else:
        print("Record not found.")

def main():
    while True:
        print("\n\nThis is a menu driven program\n"
              "\t1------To Write in a file\n\t"
              "2------To append in the file\n\t"
              "3------To read from the file\n\t"
              "4------To update the file\n\t"
              "5------To search in the file\n\t"
              "6------To delete from the file\n\t"
              "7------To exit\n")
        choice = input("Enter your choice: ")
        if choice == "1":
            write()
        elif choice == "2":
            append()
        elif choice == "3":
            read()
        elif choice == "4":
            update()
        elif choice == "5":
            search()
        elif choice == "6":
            delete()
        elif choice == "7":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()

