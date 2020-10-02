known_users = ["Alice", "John", "Julie", "Dave", "Beth"]

while True:
    print("Hi! My name is Travis")
    name = input("What is your name? ").strip().capitalize()

    if name in known_users:
        print("Hello {}".format(name))
        remove = input("Do you want to be removed from the system? (y/n)").lower().strip()
        if remove == ("y").lower():
         known_users.remove(name)
         print(known_users)
         print("{}, you have now been removed from the system".format(name))
    
        elif remove == ("n").lower():
         print("No problem {}, you have been retained on the system".format(name))
    else:
        print("Hello {}".format(name))
        append = input("Do you want to be added to the system? (y/n)").lower().strip()
        if append == ("y"):
            known_users.append(name)
            print(known_users)
            print("{}, you have now been added to the system".format(name))
        elif append == ("n"):
            print("No worries {}, you have not been added to the system".format(name))
            print(known_users)
