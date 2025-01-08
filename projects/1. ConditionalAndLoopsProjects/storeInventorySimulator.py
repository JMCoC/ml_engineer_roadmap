inventory = []

def showMenu():
    option = 0
    while option != 4:
        print("-" * 20)
        print("1. Add an item to the inventory")
        print("2. Remove an item from the inventory")
        print("3. Show the inventory")
        print("4. Exit")
        print("-" * 20)
        while True:
            try:
                option = int(input("Enter your choice: "))
                break
            except ValueError:
                print("Please enter a valid number.")
                continue
        if option == 1:
            addItem()
        elif option == 2:
            removeItem()
        elif option == 3:
            showInventory()
        elif option == 4:
            print("Exiting the program")
        else:
            print("Invalid option")

def addItem():
    item = input("Enter the item to add: ")
    if item not in inventory:
        inventory.append(item)
        print(f"{item} added to the inventory")
    else:
        print(f"{item} is already in the inventory")


def removeItem():
    item = input("Enter the item to remove: ")
    if item in inventory:
        inventory.remove(item)
        print(f"{item} removed from the inventory")
    else:
        print(f"{item} not found in the inventory")

def showInventory():
    if inventory:
        print("Inventory:")
        for item in inventory:
            print(f"- {item}")
    else:
        print("The inventory is empty.")


if __name__ == "__main__":
    showMenu()