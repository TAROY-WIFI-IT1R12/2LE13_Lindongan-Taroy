try:
    f = open("personaldiary.txt","x")
except FileExistsError:
    print("File already existed")
   
while True:
   
    print("Personal Diary System")
    print("[1] Write a message")
    print("[2] Add a message")
    print("[3] Read a message")
    print("[4} Update a message")
    print("[5] Exit")
   
    choice = input("Enter your choice: ")
   
    if choice == "1":
        message = input("Enter your message: ")
        with open("personaldiary.txt", "w") as f:
            f.write(message + "\n")
            print("Message written to diary.")
    elif choice == "2":
        message = input("Enter your message: ")
        with open("personaldiary.txt", "a") as f:
            f.write(message + "\n")
        print("Message added to diary.")
    elif choice == "3":
        with open("personaldiary.txt", "r") as f:
            content = f.read()
            print("Diary Content:")
            print(content)
    elif choice == "4":
        with open("personaldiary.txt", "r") as f:
            content = f.readlines()
            
        print("Current Diary Content:")
        for idx, line in enumerate(content, start=1):
            print(f"{idx}. {line.strip()}")
        
        line_number = int(input("Enter the line number to update: "))
        if 1 <= line_number <= len(content):
            new_message = input("Enter the new message: ")
            content[line_number - 1] = new_message + "\n"
            with open("personaldiary.txt", "w") as f:
                f.writelines(content)
            print("Message updated in diary.")
        else:
            print("Invalid line number.")
    elif choice == "5":
        print("Exiting Personal Diary System.")
        break
    else:
        print("Invalid choice. Please try again.")
        
    
    
