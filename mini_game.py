command = ""
started = False
while True
    command = input(">").lower()
    if command== "start":
        if started:
            print("Car already started")
        else:
            started = True
            print("Car started")          

    elif command == "stop":
        if not started:
            print("Car already stopped")
        else:
            started = False         
        print("car band ho gayi")
    elif command == "help":
        print("""
        start - chalu karne ke liye
        stop - band karne ke liye
        quit - to quit     
        """)
    elif command == "quit":
        break
    else:
        print("क्षमा कीजिए ")
