from sys import exit

Candy = False
Door_key = False
Treasure_key = False

def die(sentence):
    print(sentence)
    print("GAME OVER!")
    exit(1)

def death_room():
    die("You enter in the room and immediately die...")

def candy_room():
    
    global Candy

    print("\nYou entered in a room.")

    while 1:
    
        if Candy == False:
            print("\nThere is a big candy on the floor.")
            print("The flavour of the candy is stegosaur...Yummy!")

        print("There are three doors: one at north, one at south and one at west.")
        
        print("What do you want to do?")

        print("1. North")
        print("2. West")
        print("3. South")
        if Candy == False:
            print("4. Take the Candy")

        choice = int(input("> "))

        try:
            if choice == 1:
                key_room()
            elif choice == 2:
                dino_room()
            elif choice == 3:
                death_room()
            elif (choice == 4) and (Candy == False):
                print("You took the candy with you.")
                Candy = True
            else:
                print("The number you put is not a valid choice.")
        except ValueError:
            print("You have to type a number!")

def dino_room():

    global Candy
    global Treasure_key

    sleeping_dino = False

    print("\nYou are in a room with an angry, giant dinosaur!")
    print("Fortunately, until you stay still, it cannot see you.")
    print("In one of its little arm, it grabs a little key.")
    print("There is a door at North and a door at East.")

    print("\nWhat do you want to do?")
    
    while True:
        print("1. North.")
        print("2. East.")
        if Treasure_key == False:
            print("3. Grab the dinosaur's key.")
        if Candy == True:
            print("4. Launch the candy to the dinosaur!")

        choice = int(input("> "))

        try:
            if choice == 1:
                if sleeping_dino == False:
                    die("The dinosaur eats you like a sandwich!")
                else:
                    start_room()

            elif choice == 2:
                if sleeping_dino == False:
                    die("The dinosaur eats you like a sandwich!")
                else:
                    candy_room()

            elif choice == 3 and Treasure_key == False:
                if sleeping_dino == False:
                    die("The dinosaur eats you like a sandwich!")
                else:
                    Treasure_key = True
                    print("You took the small key from the dinosaur!")

            elif choice == 4 and Candy == True:
                Candy = False
                print("The dinosaur seems to like your candy!")
                print("...")
                print("...")
                print("The dinosaur finish the candy.")
                print("...")
                print("...")
                print("And now it fall asleep! Pfeuuu!")
                sleeping_dino = True

            else:
                print("You have to put a number among the listed choices!")
        except ValueError:
            print("You must type a number!!")

def treasure_room():
    print("You are in the treasure room.")

def key_room():

    global Door_key

    print("\nYou entered in a big empty room.")

    while 1:
        if Door_key == False:
            print("Now, you can see a key in the middle of the room.")

        print("There is one door at South, and one door at West.")
    
        print("What do you want to do?")
        print("1. South")
        print("2. West")
        if Door_key == False:
            print("3. Take the key")

        choice = int(input("> "))

        try:
            if (choice == 3) and (Door_key == False):
                print("You took the key with you.")
                Door_key = True
            elif choice == 1:
                candy_room()
            elif choice == 2:
                start_room()
            else:
                print("The number you put is not a valid choice.")
        except ValueError:
            print("You have to type a number!")
	     

    

def start_room():

    global Door_key

    while 1:
        print("\nYou are in an empty room with three doors.")
        print("Which door you want to open?")
        print("1. West")
        print("2. East")
        print("3. South")
        
        try:
            choice = int(input("> "))
            
            if choice == 1 and Door_key == True:
                treasure_room()
            elif choice == 1 and Door_key == False:
                print("The door is closed.")
            elif choice == 2:
                key_room()
            elif choice == 3:
                dino_room()
            else:
                print("You have to insert a value between 1 and 3.") 
        except ValueError:
            print("You have to type a number!")

start_room()

