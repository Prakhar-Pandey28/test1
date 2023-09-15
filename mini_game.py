command = ""
while command.lower() !="quit":
    command = input(">").lower()
    if command== "start":
        print("Chalu ho gayi.. chal di!")
    elif command == "stop":
        print("car band ho gayi")
    elif command == "help":
        print("""
        Start - chalu karne ke liye
        stop - band karne ke liye
        quit - to quit
        """)
    elif command =="quit": 
        break
    else:
        print("Sorry, itna padha likha nhi hu")
