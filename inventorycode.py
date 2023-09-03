class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item_name, quantity):
        if item_name in self.items:
            self.items[item_name] += quantity
        else:
            self.items[item_name] = quantity

    def remove_item(self, item_name, quantity):
        if item_name in self.items:
            if self.items[item_name] >= quantity:
                self.items[item_name] -= quantity
                if self.items[item_name] == 0:
                    del self.items[item_name]
            else:
                print(f"Error: Not enough {item_name} in inventory.")
        else:
            print(f"Error: {item_name} not found in inventory.")

    def view_inventory(self):
        print("Current Inventory:")
        for item, quantity in self.items.items():
            print(f"{item}: {quantity}")

def main():
    my_inventory = Inventory()

    while True:
        print("\nOptions:")
        print("1. Add item to inventory")
        print("2. Remove item from inventory")
        print("3. View inventory")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            item_name = input("Enter the item name: ")
            quantity = int(input("Enter the quantity: "))
            my_inventory.add_item(item_name, quantity)
            print(f"{quantity} {item_name}(s) added to inventory.")
        
        elif choice == '2':
            item_name = input("Enter the item name: ")
            quantity = int(input("Enter the quantity to remove: "))
            my_inventory.remove_item(item_name, quantity)
            print(f"{quantity} {item_name}(s) removed from inventory.")
        
        elif choice == '3':
            my_inventory.view_inventory()
        
        elif choice == '4':
            print("Exiting program.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
