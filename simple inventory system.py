import sqlite3

# Database setup
def setup_database():
    connection = sqlite3.connect('inventory.db')
    cursor = connection.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS inventory (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        quantity INTEGER NOT NULL,
        price REAL NOT NULL
    )''')
    
    connection.commit()
    connection.close()

# Add a new item to the inventory
def add_item(name, quantity, price):
    connection = sqlite3.connect('inventory.db')
    cursor = connection.cursor()
    
    cursor.execute('INSERT INTO inventory (name, quantity, price) VALUES (?, ?, ?)', (name, quantity, price))
    
    connection.commit()
    connection.close()
    print(f"Item '{name}' added successfully!")

# Update an existing item in the inventory
def update_item(item_id, name=None, quantity=None, price=None):
    connection = sqlite3.connect('inventory.db')
    cursor = connection.cursor()

    if name:
        cursor.execute('UPDATE inventory SET name = ? WHERE id = ?', (name, item_id))
    if quantity:
        cursor.execute('UPDATE inventory SET quantity = ? WHERE id = ?', (quantity, item_id))
    if price:
        cursor.execute('UPDATE inventory SET price = ? WHERE id = ?', (price, item_id))

    connection.commit()
    connection.close()
    print(f"Item with ID {item_id} updated successfully!")

# Delete an item from the inventory
def delete_item(item_id):
    connection = sqlite3.connect('inventory.db')
    cursor = connection.cursor()
    
    cursor.execute('DELETE FROM inventory WHERE id = ?', (item_id,))
    
    connection.commit()
    connection.close()
    print(f"Item with ID {item_id} deleted successfully!")

# View all items in the inventory
def view_inventory():
    connection = sqlite3.connect('inventory.db')
    cursor = connection.cursor()
    
    cursor.execute('SELECT * FROM inventory')
    items = cursor.fetchall()
    
    connection.close()
    
    print("\nCurrent Inventory:")
    print("ID | Name | Quantity | Price")
    print("---------------------------------")
    for item in items:
        print(f"{item[0]} | {item[1]} | {item[2]} | {item[3]}")

# Search for items in the inventory
def search_items(keyword):
    connection = sqlite3.connect('inventory.db')
    cursor = connection.cursor()
    
    cursor.execute('SELECT * FROM inventory WHERE name LIKE ?', ('%' + keyword + '%',))
    items = cursor.fetchall()
    
    connection.close()
    
    print("\nSearch Results:")
    print("ID | Name | Quantity | Price")
    print("---------------------------------")
    for item in items:
        print(f"{item[0]} | {item[1]} | {item[2]} | {item[3]}")

# Main menu
def main():
    setup_database()
    while True:
        print("\nSimple Inventory Management System")
        print("1. Add New Item")
        print("2. Update Existing Item")
        print("3. Delete Item")
        print("4. View Inventory")
        print("5. Search Items")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter item name: ")
            quantity = int(input("Enter item quantity: "))
            price = float(input("Enter item price: "))
            add_item(name, quantity, price)
        elif choice == '2':
            item_id = int(input("Enter item ID to update: "))
            name = input("Enter new name (leave blank to skip): ") or None
            quantity = input("Enter new quantity (leave blank to skip): ")
            quantity = int(quantity) if quantity else None
            price = input("Enter new price (leave blank to skip): ")
            price = float(price) if price else None
            update_item(item_id, name, quantity, price)
        elif choice == '3':
            item_id = int(input("Enter item ID to delete: "))
            delete_item(item_id)
        elif choice == '4':
            view_inventory()
        elif choice == '5':
            keyword = input("Enter search keyword: ")
            search_items(keyword)
        elif choice == '6':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
