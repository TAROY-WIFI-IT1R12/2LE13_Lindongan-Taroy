try:
    f = open("personaldiary.txt","x")
except FileExistsError:
    print("File already existed")
   
while True:
   
    print("Personal Diary System")
    print("[1] Write a message")
    print("[2] Add a message")
    print("[3] Exit")
   
    choice = input("Enter your choice: ")
   
    if choice == "1":
        message = input("Enter your message: ")
        with open("personaldiary.txt","w") as f:
            f.write(message + "\n")
        print("Message written to diary.")