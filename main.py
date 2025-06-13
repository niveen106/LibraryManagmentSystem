from models.library import Library
from models.users import Users 
from exceptions.CustomeExceptions import ItemNotAvailableError, UserNotFoundError, FileNotFoundError, ItemNotFoundError



library = Library() #create a Library object
library.load_users() #load users from 'users.json' file
library.load_items() #load items from 'items.json' file

while True:
    print ("***** Welcome to the Library System ******")
    print("1. View all available items\n"
            "2. Search item by title or type\n"
            "3. Register as a new user\n"
            "4. Borrow an item\n"
            "5. Reserve an item\n"
            "6. Return an item\n"
            "7. Exit and Save\n")
    try:
        choice = input("Please enter your choice:")
        if not choice.isdigit():
            raise ValueError("Input must be a digit.")
        choice = int(choice)
        if choice < 1 or choice > 7:
            raise ValueError("Input must be an integer number between 1 and 7.")
        if choice ==1:
            print("Available items in the Library:")
            library.display_items()

        elif choice == 2:
            search_query = input("Enter the title or type of the item you want to search for:")
            library.search_item(search_query)  # Search for items by title or type

        elif choice == 3:
            name = input("Enter your name:")
            user_id = name[0].lower() + str(len(library.users) + 1) # Generate a unique user ID , first letter of the name + number of users + 1
            library.add_user(Users(user_id, name))  # Create a new user and add to the library
            print(f"User {name} registered successfully with ID: {user_id}.")
        elif choice == 4:
            print("Available items and their IDs:")
            for i in library.items.values():
              print(f"- {i.item_id}: {i.title}")
            user_id = input("Enter your user ID:")
            item_id = input("Enter the item ID you want to borrow:")  
            library.borrow_item(user_id, item_id)
            print("Item borrowed successfully.")
        elif choice == 5:
            user_id = input("Enter your user ID:")
            item_id = input("Enter the item ID you want to reserve:")
            library.reserve_item(user_id, item_id)
            print("Item reserved successfully.")
        elif choice == 6:
            user_id = input("Enter your user ID:")
            item_id = input("Enter the item ID you want to return:")
            library.return_item(user_id, item_id)
            print("Item returned successfully.")
        elif choice == 7:
            library.save_data()  # Save the library data to files 
            print("The data has been saved successfully. Goodbye!")
            print("Thank you for using the Library System. Have a great day!\n")
            break
        else:
            print("Invalid choice. Please try again.")  
    except(ItemNotAvailableError, UserNotFoundError, FileNotFoundError, ItemNotFoundError) as e:
        print(f"Error: {e}") 
        continue     
    except ValueError as e:
        print(f"Invalid input: {e}.")
        continue
    except KeyboardInterrupt:
        print("\nExiting the program.")
        break 
