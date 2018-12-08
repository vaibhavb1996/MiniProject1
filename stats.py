from Database import MyDatabase
db = MyDatabase()

choice = 0
while choice is not 5:
	print("This program lets you do the following:")
	print("1. Display all data")
	print("2. Display all tags")
	print("3. Display all handles used")
	print("4. Avg no. of images per session")
	print("5. Exit\n")

	choice = int(input("Enter your choice: "))
	if choice is 1:
		ID = input("Enter User ID: ")
		db.get_all_data(ID)
	else:
		if choice is 2:
			db.get_all_tags()
		else:
			if choice is 3:
				db.get_all_handles()
			else:
				if choice is 4:
					db.avg_images()
				else:
					if choice is 5:
						print("Thanks for using the program. Ciao!")
						exit()
					else:
						print("Wrong choice, Try again!")
db.close_connection()

