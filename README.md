Library Management System

A basic library system using Python and OOP. Users can register, borrow, return, and reserve items (Books, DVDs, Magazines). Data is stored in `users.json` and `items.json`.

****How to Run
Use **Command Prompt (cmd)** for best results:
1.Navigate to the project directory:
    ```bash
    cd LibraryProject_NiveenNasereddin
    ```
2.  Run the main application:

    ```bash
    python main.py
    ```
3. Interact with the CLI:
    Follow the on-screen menu to perform various library operations.


**Note**: 
If you run the program from the VS Code integrated terminal, sometimes it may not detect the JSON files correctly, especially if relative paths are involved or the working directory isn't set to the root of the project. If that happens, use cmd instead.



## Project Structure

```
LibraryProject_NiveenNasereddin
├── main.py
├── items.json
├── users.json
├── README.md
├── models/
│   ├── __init__.py
│   ├── library.py
│   ├── library_item.py
│   ├── items.py
│   └── users.py
└── exceptions/
    └── CustomExceptions.py
```

*   `main.py`: Contains the main CLI loop and interaction logic.
*   `items.json`: Stores initial and updated library item data.
*   `users.json`: Stores initial and updated user data.
*   `models/`: Contains classes defining the core entities of the library system.
    *   `library.py`: Manages library operations (add/remove items/users, borrow, return, reserve, search).
    *   `library_item.py`: Defines the abstract `LibraryItem` class and `Reservable` interface.
    *   `items.py`: Contains concrete implementations of `LibraryItem` (Book, Magazine, DVD).
    *   `users.py`: Defines the `Users` class.
*   `exceptions/`: Contains custom exception classes.
    *   `custom_exceptions.py`: Defines `ItemNotAvailableError`, `UserNotFoundError`, `ItemNotFoundError`.


