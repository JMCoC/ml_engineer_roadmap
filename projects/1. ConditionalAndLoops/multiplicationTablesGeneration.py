def multiplicationTablesGeneration():
    while True:
        try:
            num = int(input("Enter a number: "))
            break
        except ValueError:
            print("Please enter a valid number.")
            continue
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")
    print("-" * 20)

if __name__ == "__main__":
    continue_program = "y"
    while continue_program == "y":
        multiplicationTablesGeneration()
        while True:
            continue_program = input("Do you want to continue? (y/n): ").lower()
            if continue_program == "y" or continue_program == "n":
                break
            else:
                print("Please enter a valid input.")
                continue