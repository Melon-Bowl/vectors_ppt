# Python program to demonstrate the use of vectors

from vector import Vector
from time import sleep
import os


# Clear console output function
clear = lambda : os.system( 'cls' ) # Use a lambda function because I can

if __name__ == "__main__":
    clear()
    print("\u001b[34;1m### Welcome ###\u001b[0m")

    print("\u001b[34;1m\nName of the first vector?\u001b[0m")
    name = input("\u001b[34m  >>\u001b[0m")
    print("\n\u001b[33;1mCreating vector %s\u001b[0m" % name)

    vector1 = Vector(name) # Creating first vector
    vector1.show() # Show empty vector

    sleep(1)

    clear()

    print("\u001b[34;1m\nName of the second vector?\u001b[0m")
    name2 = input("\u001b[34m  >>\u001b[0m")
    print("\n\u001b[33;1mCreating vector %s\u001b[0m" % name2)

    vector2 = Vector(name2) # Creating second vector
    vector2.show()

    sleep(1)

    clear()

    while True:

        clear()

        print("\u001b[34;1m\nAdd data to vector %s.\u001b[0m" % name)

        try:
            data = int(input("\u001b[34m  >>\u001b[0m"))
            vector1.insertData(data)
        except ValueError:
            print("\n\u001b[31;1mInvlid input. Please input an integer.\u001b[0m")

        print("\u001b[34;1m\nAdd more? (y/n)\u001b[0m")
        choice = input("\u001b[34m  >>\u001b[0m")

        if choice.lower() != 'y':
            print("\n\u001b[33;1mHere is %s:\u001b[0m" % name)
            vector1.show()
            sleep(3)
            break

    while True:

        clear()

        print("\u001b[34;1m\nAdd data to vector %s.\u001b[0m" % name2)

        try:
            data = int(input("\u001b[34m  >>\u001b[0m"))
            vector2.insertData(data)
        except ValueError:
            print("\n\u001b[31;1mInvlid input. Please input an integer.\u001b[0m")
    
        print("\u001b[34;1m\nAdd more? (y/n)\u001b[0m")
        choice = input("\u001b[34m  >>\u001b[0m")

        if choice.lower() != 'y':
            print("\n\u001b[33;1mHere is %s:\u001b[0m" % name2)
            vector2.show()
            sleep(3)
            break
    
    print("\u001b[33;1m\nSetup complete.\u001b[0m")
    print("\u001b[34;1m\nWhat now?\u001b[0m")

    while True:
        vector1.showOptions()
        choice = input("\u001b[34m  >>\u001b[0m")
        clear()

        leave = False
        
        try:
            if choice == '1':
                vector1.add(vector2)
            elif choice == '2':
                vector1.subtract(vector2)
            elif choice == '3':
                vector1.multiply(vector2)
            elif choice == '4':
                vector1.divide(vector2)
            elif choice == '5':
                vector1.dotProduct(vector2)
            elif choice == '6':
                print("\u001b[34;1m\nWhich vector would you like to remove data from?\u001b[0m \u001b[35;1m1: {} \u001b[34;1mor \u001b[35;1m2: {}\u001b[34;1m?\u001b[0m".format(name, name2))
                vectorChoice = input("\u001b[34m  >>\u001b[0m")
                if vectorChoice == '1':
                    clear()
                    vector1.show()
                    print("\u001b[34;1m\nWhat is the index of the item you would like to delete?")
                    index = int(input("\u001b[34m  >>\u001b[0m"))
                    vector1.removeData(index)
                    
                    print("\u001b[34;1m\nDelete the data from the same index in %s? (y/n)" % name2)
                    userChoice = input("\u001b[34m  >>\u001b[0m")
                    
                    if userChoice.lower() == 'y': vector2.removeData(index)
                    
                    print("\u001b[33;1m\nUpdated vectors:\u001b[0m")
                    vector1.show()
                    vector2.show()

                elif vectorChoice == '2':
                    clear()
                    vector2.show()
                    print("\u001b[34;1m\nWhat is the index of the item you would like to delete?")
                    index = int(input("\u001b[34m  >>\u001b[0m"))
                    vector2.removeData(index)

                    print("\u001b[34;1m\nDelete the data from the same index in %s? (y/n)" % name)
                    userChoice = input("\u001b[34m  >>\u001b[0m")
                    
                    if userChoice.lower() == 'y': vector1.removeData(index)

                    print("\u001b[33;1m\nUpdated vectors:\u001b[0m")
                    vector1.show()
                    vector2.show()

                else:
                    print("\u001b[31;1m\nInvalid input.")
            elif choice == '7':
                print("\u001b[33;1m\n### Now exiting. Thank you for using the program :) ###\u001b[0m")
                leave = True
                exit()
        except:
            if not leave:
                print("\u001b[31;1m\nAn error has occured. Please make sure that both arrays are the same size and try again.\u001b[0m")
            else:
                exit()
            