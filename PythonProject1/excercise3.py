numbers = []

while True:
    user_input = input("Enter a number (press Enter to quit): ")

    if user_input == "":
        break

    numbers.append(float(user_input))

print("Smallest number:", min(numbers))
print("Largest number:", max(numbers))
