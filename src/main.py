print('E-Sports Manager')
class MainScreen:
    
    def display_menu():
        print("===== Welcome! ======")
        print("[1] Register")
        print("[2] View / Edit Teams")
        print("[3] Exit")
        print("=====================")

    def option1():
        print("You selected Option 1")

    def option2():
        print("You selected Option 2")

    def option3():
        print("You selected Option 3")

    # Main program
    while True:
        display_menu()

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            option1()
        elif choice == "2":
            option2()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
