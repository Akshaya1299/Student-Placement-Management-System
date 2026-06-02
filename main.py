students = []

while True:
    print("\n--- Student Placement Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        usn = input("Enter USN: ")
        branch = input("Enter Branch: ")
        cgpa = input("Enter CGPA: ")

        student = {
            "name": name,
            "usn": usn,
            "branch": branch,
            "cgpa": cgpa
        }

        students.append(student)

        file = open("students.txt", "a")
        file.write(name + "," + usn + "," + branch + "," + cgpa + "\n")
        file.close()

        print("Student Added Successfully")

    elif choice == "2":
        try:
            file = open("students.txt", "r")

            for line in file:
                data = line.strip().split(",")

                print("\nName:", data[0])
                print("USN:", data[1])
                print("Branch:", data[2])
                print("CGPA:", data[3])

            file.close()

        except:
            print("No students found")

    elif choice == "3":
        break

    else:
        print("Invalid Choice")