# Inventory_Management_System
Inventory Management System :
This project is a console-based application that allows users to manage inventory efficiently. It uses Python for logic implementation and SQLite as the database for storing inventory data.

Key Features:
Database Setup: The setup_database function initializes the SQLite database and creates a table named inventory if it doesn't already exist. This ensures the system is always ready to operate.

Adding Items: The add_item function inserts new items into the database with attributes like name, quantity, and price. This simulates adding new stock to an inventory.

Updating Items: The update_item function allows modification of existing item details such as name, quantity, or price, identified by their unique ID.

Deleting Items: The delete_item function removes items from the inventory based on their ID, which is useful for managing obsolete or unavailable stock.

Viewing Inventory: The view_inventory function retrieves and displays all items in a structured format, making it easy to check the current stock.

Searching Items: The search_items function filters inventory items based on a keyword, allowing quick access to relevant data.

Interactive Menu: The main function presents a user-friendly menu to interact with the system, ensuring smooth navigation between operations.


Technologies Used

Python: For the application logic and user interface.

SQLite: For storing inventory data persistently.

This project demonstrates my ability to integrate Python with a database for CRUD (Create, Read, Update, Delete) operations.

It highlights skills like database management, SQL query handling, and implementing user-friendly interfaces.

The modular design ensures that each function performs a specific task, promoting readability and maintainability.
