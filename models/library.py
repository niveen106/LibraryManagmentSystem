import json
import os
from .items import Book, Magazine, DVD
from .users import Users
from exceptions.CustomeExceptions import ItemNotAvailableError, UserNotFoundError, FileNotFoundError, ItemNotFoundError
from models.library_item import LibraryItem, Reservable
class Library:
    def __init__(self):
        self.users = {}
        self.items = {}

#load users from 'users.json' file
    def load_users(self):
        try:
            if not os.path.exists('users.json'):
                raise FileNotFoundError('users.json')
            
            with open(os.path.join(os.getcwd(), 'users.json')) as read:
                users_data = json.load(read)
                for user in users_data:
                    obj = Users(user_id=user["user_id"], name=user["name"])
                    obj.borrowed_items = user.get("borrowed_items", [])
                    self.users[obj.user_id] = obj  # Add the user to the library's users dictionary
        except Exception as e:
            print(f"Error loading users: {e}")

        else:
            print("Users loading successfully.")                                  

#load items from 'items.json' file
    def load_items(self):
        try:
            if not os.path.exists('items.json'):
                raise FileNotFoundError('items.json')
            
            with open(os.path.join(os.getcwd(), 'items.json')) as read:
                items_data = json.load(read)
                for item in items_data:
                    item_type = item.pop('type')
                    if item_type.lower() == 'book':
                        itm = Book(**item) # Create a Book object 
                    elif item_type.lower() == 'magazine':
                        itm = Magazine(**item) # Create a Magazine object
                    elif item_type.lower() == 'dvd':
                        itm = DVD(**item) # Create a DVD object
                    else:
                        print(f"Unknown item type: {item['type']}, skipping...")
                        continue
                    # Add the item to the library's items dictionary
                    self.items[itm.item_id] = itm            
        except Exception as e:
            print(f"Error loading items: {e}")
        else:
            print("Items loading successfully.")

# Add a new user to the library
    def add_user(self, usr):
        self.users[usr.user_id]=usr 

#remove a user from the library
    def remove_user(self, user_id):
        if user_id in self.users:
            del self.users[user_id]
            print(f"User {user_id} removed successfully.")
        else:
            raise UserNotFoundError(f"User with ID {user_id} not found.")
        

# Add a new item to the library
    def add_item(self, item):
        self.items[item.item_id] = item

# Remove an item from the library
    def remove_item(self, item_id):
        if item_id in self.items:
            del self.items[item_id]
            print(f"Item {item_id} removed successfully.")
        else:
            raise ItemNotFoundError(f"Item with ID {item_id} not found.")

    def save_data(self):
        try:
            items_list = []
            for item in self.items.values():
                item_data = item.__dict__.copy()
                item_data['type'] = type(item).__name__  # Add the type of the item
                items_list.append(item_data)

            with open('items.json', 'w') as f:
                json.dump(items_list, f, indent=4)

        
            users_list = []
            for user in self.users.values():
                user_data = {
                    "user_id": user.user_id,
                    "name": user.name,
                    "borrowed_items": user.borrowed_items
                }
                users_list.append(user_data)

            # حفظ المستخدمين في ملف users.json
            with open('users.json', 'w') as f:
                json.dump(users_list, f, indent=4)

        except Exception as e:
            print(f"Error saving data: {e}")



#borrow an item from the library
    def borrow_item(self, user_id, item_id):
        if user_id not in self.users:
            raise UserNotFoundError(f"User with ID {user_id} not found.")
        if item_id not in self.items:
            raise ItemNotFoundError(f"Item with ID {item_id} not found.")
        
        item = self.items[item_id]
        user = self.users[user_id]

        if not item.is_available:
            raise ItemNotAvailableError(f"{item.title} is not available for borrowing.")

        item.is_available = False
        user.borrowed_items.append(item.item_id)
        print(f"{user.name} has borrowed {item.title}.")

# Return an item to the library
    def return_item(self, user_id, item_id):
        if user_id not in self.users:
            raise UserNotFoundError(f"User with ID {user_id} not found.")
        if item_id not in self.items:
            raise ItemNotFoundError(f"Item with ID {item_id} not found.")
        
        item = self.items[item_id]
        user = self.users[user_id]

        if item_id not in user.borrowed_items:
            raise ItemNotAvailableError(f"{item.title} was not borrowed by {user.name}.")

        item.is_available = True
        user.borrowed_items.remove(item.item_id)
        print(f"{user.name} has returned {item.title}.")

# reserve an item in the library
    def reserve_item(self, user_id, item_id):
        if user_id not in self.users:
            raise UserNotFoundError(f"User with ID {user_id} not found.")
        if item_id not in self.items:
            raise ItemNotFoundError(f"Item with ID {item_id} not found.")
        
        item = self.items[item_id]
        user = self.users[user_id]

        if not isinstance(item, Reservable):
            print(f"{item.title} cannot be reserved.")
            return

        try:
            item.reserve(user)
        except ItemNotAvailableError as e:
            print(f"Error reserving item: {e}")

# display all items in the library
    def display_items(self):
        if not self.items:
            print("No items available in the library.")
            return
        for item in self.items.values():
            item.display_info()

# search for an item by title or author or ISBN
    def search_item(self, keyword):
            found_items = []
            for item in self.items.values():
                if keyword.lower() in item.title.lower() or keyword.lower() in item.auther.lower():
                    found_items.append(item)
            if not found_items:
                print(f"No items found matching '{keyword}'")
            else:
                for item in found_items:
                    item.display_info()

