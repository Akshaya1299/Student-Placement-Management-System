students = []

while True:
    print("\n--- Student Placement Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        usn = input("Enter USN: ")
        branch = input("Enter Branch: ")
        cgpa = input("Enter CGPA: ")

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
        search_usn = input("Enter USN to Search: ")

        try:
            file = open("students.txt", "r")
            found = False

            for line in file:
                data = line.strip().split(",")

                if data[1] == search_usn:
                    print("\nStudent Found")
                    print("Name:", data[0])
                    print("USN:", data[1])
                    print("Branch:", data[2])
                    print("CGPA:", data[3])
                    found = True

            if found == False:
                print("Student Not Found")

            file.close()

        except:
            print("No students found")

    elif choice == "4":
        delete_usn = input("Enter USN to Delete: ")

        file = open("students.txt", "r")
        lines = file.readlines()
        file.close()

        file = open("students.txt", "w")

        found = False

        for line in lines:
            data = line.strip().split(",")

            if data[1] != delete_usn:
                file.write(line)
            else:
                found = True

        file.close()

        if found:
            print("Student Deleted Successfully")
        else:
            print("Student Not Found")

    elif choice == "5":
        break

    else:
        print("Invalid Choice")