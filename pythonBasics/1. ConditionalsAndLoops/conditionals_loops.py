for i in range(10):
    print(i+1)

num = 10
while num >= 1:
    print(num)
    num -= 1


while True:
    try:
        age = int(input("Write your age: "))
        break
    except ValueError:
        print("Please enter a valid number.")
        continue
if age >= 18:
    print("You can vote")
else:
    print("You can't vote")