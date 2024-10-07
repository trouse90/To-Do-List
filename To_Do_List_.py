import time # The terminal can output information very quickly and can make it hard at times to figure out where new input is. I like to use time to give the user a chance to see the output coming.


list = {} #We are going to create a dictionary and leave it blank to accept input from user.
y = 1 #"y" will be incrementing by 1

# I decided I might add more functions to this program later, and rather  than starting on a page that imediatly To Do List we will start with an options menu.
# This begins the program loop and asks the user what they would like to do
while True:
    print("a. To Do List")
    print("b. Future Option")
    print("c. Future Option")
    print("e. Stop")
    
    print("")
    time.sleep(2)
    x = input("Enter choice: ")
   
    if x == "e":
        print("bye now")
        break
   
    if x == "a":
        while True:
            x = input("New Note: ")
        
            if x == "e":
                print("Exiting")
                print("")
                break
            if x == "b":
                    print("Still under development")
            if x == "c":
                    print("Still under development")

            list[y] = x
            y += 1
            print("Your To-Do List")

            for key, task in list.items():
                print(key, task)
                   
    else:
        print("")
        time.sleep(2)
        print("Not an option")
