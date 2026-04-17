from tracker import add_scholarship, view_scholarships, total_amount

def menu():
    while True:
        print("\nScholarship Tracker")
        print("1. Add Scholarship")
        print("2. View Scholarships")
        print("3. Total Amount")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Scholarship name: ")
            deadline = input("Deadline: ")
            amount = float(input("Amount: "))
            add_scholarship(name, deadline, amount)

        elif choice == "2":
            view_scholarships()

        elif choice == "3":
            print("Total Amount:", total_amount())

        elif choice == "4":
            break

        else:
            print("Invalid choice")

menu()
