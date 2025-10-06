admins = ["Ahmed", "Osama", "Ali", "Manal", "Mahmoud", "Rahma", "Enas"]
password = "pleaseAdd@12345"

name = input("What is your name? ").strip().capitalize()
if name in admins:
    print(f"Hello {name}!, Welcome Back")
    action = input("What would you like to do next? (update/delete)").lower()
    if action == "update":
        new_name  = input("Enter the new name: ").strip().capitalize()
        admins[admins.index(name)]= new_name
        print("Name successfully updated")
        print(admins)
    elif action == "delete":
        verify = input("are you sure you want to delete this admin? (yes/no) ")
        if verify == "yes":
            admins.remove(name)
            print("Admin has successfully been deleted")
            print(admins)
        else:
            print("please dont play")
    else:
        print("Invalid action")
else:
    action = input("Would you like to become a admin? (yes/no)").strip().lower()
    if action == "yes":
        attempts = 5
        guess_password = input("please enter the password: ")
        while guess_password != password:
            attempts -= 1
            if attempts > 1:
                print(f"Password incorrect, you have {attempts} left ")
            elif attempts == 1:
                print("Password incorrect, you have one attempt left")
            elif attempts == 0:
                print("Incorrect password, No more attempts left. Cannot add you as a admin")
                break
            guess_password = input("please enter the password: ")
        else:
            print("added you as a admin")
            admins.append(name)
            print(admins)

    else:
        print("Did not add you as a admin")






