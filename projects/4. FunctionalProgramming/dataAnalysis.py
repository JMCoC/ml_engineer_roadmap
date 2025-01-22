from functools import reduce

sales = [
    {"product": "apple", "price": 10, "quantity": 2},
    {"product": "banana", "price": 5, "quantity": 5},
    {"product": "cherry", "price": 15, "quantity": 1}
]

def showMenu():
    option = 0
    while option != 4:
        print("-" * 20)
        print("1. Total sales per product")
        print("2. Filter income sales per product")
        print("3. Total income")
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
            totalSales(sales)
        elif  option == 2:
            filterSales(sales)
        elif  option == 3:
            totalIncome(sales)
        elif option == 4:
            print("Exiting the program")
        else:
            print("Invalid option")

def totalSales(sales):
    myList = list(map(lambda x: {"product": x["product"], "income": x["price"] * x["quantity"]}, sales))
    print(f"Total sales: {myList}")
    

def filterSales(sales):
    option = 0
    while True:
        try:
            option = int(input("Enter the minimum income: "))
            break
        except ValueError:
            print("Please enter a valid number.")
            continue
    myFilter = filter(lambda x: x["price"] * x["quantity"] >= option, sales)
    myMap = map(lambda x: {"product": x["product"], "income": x["price"] * x["quantity"]}, myFilter)
    myList = list(myMap)
    print(f"High income sales: {myList}")

def totalIncome(sales):
    myList = reduce(lambda acc, x: acc + (x["price"] * x["quantity"]), sales, 0)
    print(f"Total income: {myList}")

showMenu()