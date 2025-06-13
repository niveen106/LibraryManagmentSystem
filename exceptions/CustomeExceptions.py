# Item not available custom exception
# This exception is raised when an item is not available in the library.
class ItemNotAvailableError(Exception):
    def __init__(self, message="Item is not available in the library."):
        self.message = message
        super().__init__(self.message)

# User not found custom exception 
# This exception is raised when a user is not found in the library system.
class UserNotFoundError(Exception):
    def __init_(self, message="User not found in the library system."):
        self.message=message
        super().__init__(self.message)

#Item not found custom exception
# This exception is raised when an item is not found in the library.
class ItemNotFoundError(Exception):
    def __init__(self, message="Item not found in the library."):
        self.message = message
        super().__init__(self.message)

#File not found custom exception
class FileNotFoundError(Exception):
    def __init__(self, filename):
        message = f"The file {filename} does not exist."
        super().__init__(message)
