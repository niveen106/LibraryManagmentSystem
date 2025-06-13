class Users:
    def __init__(self,user_id,name):
        self.user_id = user_id
        self.name = name
        self.borrowed_items = []

    def display_user_info(self):
        print(f"User ID:{self.user_id}, Name: {self.name}, No. of Borrowed Items: {len(self.borrowed_items)}")    