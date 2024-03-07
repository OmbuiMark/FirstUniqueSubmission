from FirstUniqueSubmission import FirstUnique

def main():
    first_unique = None
    
    while True:
        command = input("Enter command :    'add(x)' or 'showFirstUnique()' : ")
        
        if command.startswith("add(") and command.endswith(")"):
            number = int(command[4:-1])
            if first_unique is None:
                first_unique = FirstUnique([number])
            else:
                first_unique.add(number)
        elif command == "showFirstUnique()":
            if first_unique is not None:
                print("First unique:", first_unique.showFirstUnique())
            else:
                print("No stream data.")
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
