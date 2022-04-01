#Cole Murphy
def showEntrance(room, lever, dial):
	selectionValid = False 
	while selectionValid == False: 
		print("------------------------------------------")
		print("Welcome to the Hall.")
		print()
		print(" 1) Go to kitchen ")
		print(" 2) Go to pantry  ")
		print(" 3) Try the Door")
		print("------------------------------------------")
		selection = int(input("Select Action: "))
		if (selection in (1, 2, 3)):
			selectionValid = True 
		else:
			print(" Error")
	if (selection == 1):
		room = "kitchen"
	elif (selection == 2):
		room = "pantry"
	elif (selection == 3):
		if (lever == "back" and dial == "red"):
			room = "livingRoom"
		else:
			print(" Listen Pavan you're locked in dumb dumb. Gotta solve the puzzle!!! Cole is waiting!!!!!!!!!!")
	else:
		print(" Try Again.")
	return room

def showKitchen(room, lever):
	selectionValid = False
	while selectionValid ==False:
		print("You're in the Kitchen. \n")
		print("The lever is in the " + lever + " position.")
		print("1. Pull lever forwward.")
		print("2. Pull lever back.")
		print("3. Go back to the entrance. \n")
		selection = int(input("Select Action: "))
		if (selection in (1, 2, 3)):
			selectionValid = True 
		else:
			print("Error")
	if (selection == 1):
		lever = "forward"
	elif (selection == 2):
		lever = "back"
	elif (selection == 3):
		room = "entrance"
	else:
		print(" Try Again")
	return (room, lever)

def showPantry(room, dial):
	selectionValid = False
	while selectionValid == False:
		print("You're in the pantry. \n")
		print("The dial is in the " + dial + " position.")
		print("1. Set to blue.")
		print("2. Set to red.")
		print("3. Set to green.")
		print("4. Go back to the entrance. \n")
		selection = int(input("Select Action: "))
		if (selection in (1, 2, 3, 4)):
			selectionValid = True 
		else:
			print("Error")
	if (selection == 1):
		dial = "blue"
	elif (selection == 2):
		dial = "red"
	elif (selection == 3):
		dial = "green"
	elif (selection == 4):
		room = "entrance"
	return (room, dial)
	
def showLivingroom(room, string, cheese, mouse, isInParadise):
	selectionValid = False 
	while selectionValid == False: 
		print("------------------------------------------")
		print("Welcome to the Living Room. \n")
		print(" 1. Look at Plant. ")
		print(" 2. Go to Attic.  ")
		print(" 3. Go to the Bedroom")
		if string == True:
			print(" 4. Pick up String.")
		print("------------------------------------------")
		if mouse == False:
			print(" The plant looks like it has mouse excrament all over it. Maybe take a look at it.")
		selection = int(input(" \n Select Action: "))
		if (selection in (1, 2, 3, 4)):
			selectionValid = True 
		else:
			print("Error")
		if (selection == 1):
			if mouse == True :
				print(" This plant needs some fetrilizer from a small rodent. \n")
			if not mouse:
				selectionValid = True
				isInParadise = True
		elif (selection == 2):
			room = "attic"
		elif (selection == 3):
			room = "bedroom"
		elif (selection == 4):
			string = False
			print(" \n You picked up the string.")
		else:
		  print("Try Again.")
	return (room, string, cheese, mouse, isInParadise)
	
def showAttic(room, cheese, string, cat):
	selectionValid = False
	while selectionValid == False:
		print(" \n You're in the attic. There is a lot of cheese and a mouse hole. \n")
		print(" 1. Get Cheese.")
		print(" 2. Go back to the entrance.")
		if cat == True:
			if string == False:
				print(" 3. Put string down the mouse hole.")
		selection = int(input("Select Action: "))
		if (selection in (1, 2, 3)):
			selectionValid = True 
		else:
			print("Error")
	if (selection == 1):
		cheese = False
		print("\n You took some cheese.")
	elif (selection == 2):
		room = "livingRoom"
	elif (selection == 3):
		print(" \n You put the string down the mouse hole.")
		cat = False
	else:
	  print("Try Again.")
	return (room, cheese, string, cat)

def showBedroom(room, cheese, string, cat, mouse):
	selectionValid = False
	while selectionValid == False:
		print("You're in the bedroom..... oooo la la \n ")
		if cat == True:
			print(" There is a cat staring at the mouse hole. Waiting for the mouse to come out. \n")
		print("1. Go back to the entrance. ")
		if (cat == True) and (string == False):
			print("2. Distract cat.")
		if cat == False and cheese == False:
			print(" \n The cat is no longer here. \n ")
			print("3. You have some cheese. Try and lure the mouse out of it's hole with cheese.")
		selection = int(input(" \n Select Action: "))
		if (selection in (1, 2, 3)):
			selectionValid = True 
		else:
			print("Error")
	if (selection == 1):
		room = "livingRoom"
	elif (selection == 2):
		print("The cat doesn't care about you. \n ")
	elif (selection == 3):
		if cheese == False:
			mouse = False
			print(" The mouse has taken the cheese and walked into the living room. \n ")
	else:
	  print("Try Again.")
	return (room, cheese, string, cat, mouse)

def main():
	isInParadise = False
	room = "entrance"
	lever =  "forward"
	dial  =  "green"
	string = True 
	cheese = True
	cat = True 
	mouse = True
	print("You're locked in a room. You must escape to paradise!!!!! \n Best of luck solving the puzzles!!!")
	print("------------------------------------------")
	while isInParadise == False:
		if room == "entrance":
			room = showEntrance(room, lever, dial)
		if room == "kitchen":
			room, lever = showKitchen(room, lever)
		if room == "pantry":
			room, dial = showPantry(room, dial)
		if room == "livingRoom":
			room, string, cheese, mouse, isInParadise = showLivingroom(room, string, cheese, mouse, isInParadise)
		if room == "attic":
			(room, cheese, string, cat) = showAttic(room, cheese, string, cat)
		if room == "bedroom":
			(room, cheese, string, cat, mouse) = showBedroom(room, cheese, string, cat, mouse)
	print("Welcome to paradise.")


main()
