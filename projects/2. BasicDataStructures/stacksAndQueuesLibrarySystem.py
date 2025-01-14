books = ['Data Structures', 'Loops', 'if/else statement', 'Basic Python', 'The little prince']
clients = ['Juan', 'Valeria', 'Sebastian', 'Carlos']
clientSelectedBooks = []

def showMenu():
    option = 0
    while option != 3:
        print("-" * 20)
        print("1. Next Client")
        print("2. Add Client")
        print("3. Exit")
        print("-" * 20)
        while True:
            try:
                option = int(input("Enter your choice: "))
                break
            except ValueError:
                print("Please enter a valid number.")
                continue
        if option == 1:
            if bool(clients):
                nextClient(clients[0])
                clients.pop(0)
            else:
                print("No clients")
                return
        elif  option == 2:
            addClient()
        elif option == 3:
            print("Exiting the program")
        else:
            print("Invalid option")

def nextClient(client):
    option = 0
    basket = []
    print(f"Attending client: {client}")
    while option != 4:
        print("-" * 20)
        print("1. Add book")
        print("2. Remove book")
        print("3. See Basket")
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
            addBook(basket)
        elif option == 2:
            removeBook(basket)
        elif option == 3:
            seeBasket(basket)
        elif option == 4:
            clientSelectedBooks.append((client, basket))
            print(clientSelectedBooks)
            print("Exiting the program")
        else:
            print("Invalid option")

def addClient():
    name = input("Enter the client's name: ")
    clients.append(name)
    print(f"{name} has been added to the queue.")


def addBook(basket):
    print("-" * 20)
    for book in range(len(books)):
        print(f"{book + 1}. {books[book]}")
    while True:
            try:
                option = int(input("Enter your choice: "))
                break
            except ValueError:
                print("Please enter a valid number.")
                continue

    if option <= len(books):
        if books[option - 1] in basket:
            print("This book is already in the basket.")
        else:
            basket.append(books[option - 1])

    else:
        print("Invalid Option")



def removeBook(basket):
    if basket:
        bookRemoved = basket.pop()
        print(f"Book removed: {bookRemoved}")
    else:
        print("The basket is empty, no books to remove.")


def seeBasket(basket):
    if basket:
        print("Books in the basket (from top to bottom):")
        for book in reversed(basket):
            print(f"- {book}")
    else:
        print("The basket is empty.")



showMenu()

