patient = [["A",70],["B",71],["C",72],["D",73],["E",74],["F",75]]

while True:
    print("\n1. Add a patient")
    print("2. Delete a patient")
    print("3. Search a patient")
    print("4. Display all patients")
    print("5. Count total patients")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter patient name: ")
        age = int(input("Enter patient age: "))
        patient.append([name, age])
        print("Patient added successfully.")

    elif choice == 2:
        name = input("Enter patient name to delete: ")
        found = False

        for p in patient:
            if p[0] == name:
                patient.remove(p)
                print("Patient deleted successfully.")
                found = True
                break

        if not found:
            print("Patient not found.")

    elif choice == 3:
        name = input("Enter patient name to search: ")
        found = False

        for p in patient:
            if p[0] == name:
                print("Patient found:", p)
                found = True
                break

        if not found:
            print("Patient not found.")

    elif choice == 4:
        for p in patient:
            print("Name:", p[0], "Age:", p[1])

    elif choice == 5:
        print("Total patients:", len(patient))

    elif choice == 6:
        break

    else:
        print("Invalid choice.")
