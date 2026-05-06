

students = {}

while True:
    print("\n===== SIMPLE ATTENDANCE SYSTEM =====")
    print("1. Add Student")
    print("2. Mark Attendance")
    print("3. Show Attendance")
    print("4. Save to File")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        students[name] = [0, 0]   # [present, total]
        print("Student added")

    elif choice == "2":
        name = input("Enter student name: ")

        if name in students:
            status = input("Present or Absent (p/a): ")

            if status == 'p':
                students[name][0] += 1

            students[name][1] += 1
            print("Attendance marked")
        else:
            print("Student not found")

    elif choice == "3":
        print("\nAttendance:")
        for name in students:
            present = students[name][0]
            total = students[name][1]

            if total == 0:
                percent = 0
            else:
                percent = (present / total) * 100

            if percent < 75:
                print(name, "-", round(percent, 2), "% Low")
            else:
                print(name, "-", round(percent, 2), "%")

    elif choice == "4":
        file = open("attendance_simple.txt", "w")

        for name in students:
            present = students[name][0]
            total = students[name][1]

            if total == 0:
                percent = 0
            else:
                percent = (present / total) * 100

            file.write(name + " - " + str(round(percent, 2)) + "%\n")

        file.close()
        print("Saved to attendance_simple.txt")

    elif choice == "5":
        break

    else:
        print("Invalid choice")
