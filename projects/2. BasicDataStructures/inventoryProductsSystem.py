myStore = {
    "grain":{
        "rice" :10,
        "corn" : 6,
        "oats" : 4
    },
    "fruit":{
        "apple" : 2,
        "banana": 4,
        "pineapple": 3
    },
    "drink":{
        "water" : 2,
        "soda": 1,
    }
}

def showMenu():
    option = 0
    while option != 5:
        print("-" * 20)
        print("1. Add or Update product")
        print("2. New category")
        print("3. Delete product")
        print("4. Show inventory")
        print("5. Exit")
        print("-" * 20)
        while True:
            try:
                option = int(input("Enter your choice: "))
                break
            except ValueError:
                print("Please enter a valid number.")
                continue
        if option == 1:
            addUpdateProduct()
        elif  option == 2:
            newCategory()
            print(myStore)
        elif  option == 3:
            deleteProduct()
        elif  option == 4:
            showInventory()
        elif option == 5:
            print("Exiting the program")
        else:
            print("Invalid option")

def addUpdateProduct():
    option = 0
    while option != len(myStore) + 1:
        print("-" * 20)
        for i, category in enumerate(myStore.keys(), 1):
            print(f"{i}. {category}")
        print(f"{len(myStore) + 1}. Exit")
        print("Where do you want to add your product?")
        try:
            option = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if 1 <= option <= len(myStore):
            category = list(myStore.keys())[option - 1]
            for i, (item, quantity) in enumerate(myStore[category].items(), 1):
                print(f"{i}. {item} -> {quantity}")
            newProduct = input(f"Enter the {category}: ")
            while True:
                try:
                    newQuantity = int(input("Enter the quantity: "))
                    break
                except ValueError:
                    print("Please enter a valid number.")
                    continue
            if newProduct in myStore[category]:
                print(f"Updating {newProduct}")
            else:
                print(f"Adding {newProduct}")
            myStore[category].update({newProduct: newQuantity})
        elif option == len(myStore) + 1:
            print("Exiting")
              
        else:
            print("Invalid option")

def newCategory():
    newCategory = input("Enter the new category: ")
    if newCategory in myStore:
        print(f"The category '{newCategory}' already exists.")
    else:
        myStore[newCategory] = {}
        print(f"Category '{newCategory}' added successfully.")

def deleteProduct():
    option = 0
    while option != len(myStore) + 1:
        print("-" * 20)
        for i, category in enumerate(myStore.keys(), 1):
            print(f"{i}. {category}")
        print(f"{len(myStore) + 1}. Exit")
        print("Where do you want to delete your product?")
        try:
            option = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if 1 <= option <= len(myStore):
            category = list(myStore.keys())[option - 1]
            for i, (item, quantity) in enumerate(myStore[category].items(), 1):
                print(f"{i}. {item} -> {quantity}")
            deleteProduct = input(f"Enter the {category}: ")
            if deleteProduct in myStore[category]:
                print(f"Deleting {deleteProduct}")
                del myStore[category][f"{deleteProduct}"]
            else:
                print(f"{deleteProduct} doesn't exist")
            
        elif option == len(myStore) + 1:
            print("Exiting")
            
        else:
            print("Invalid option")

def showInventory():
    for category, products in myStore.items():
        print(f"- {category}")
        for product, quantity in products.items():
            print(f"  - {product}: {quantity}")

showMenu()

