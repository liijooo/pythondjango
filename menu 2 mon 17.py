def add_numbers():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print(f"The sum is:",a+b)


def subtract_numbers():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print(f"The difference is:",a-b)


def multiply_numbers():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print(f"The product is:",a*b)


def divide_numbers():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    if b != 0:
        print(f"The division result is:",a/b)
    else:
        print("Error! Division by zero.")


def display_menu():
    print("\nMenu:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")


def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_numbers()
        elif choice == '2':
            subtract_numbers()
        elif choice == '3':
            multiply_numbers()
        elif choice == '4':
            divide_numbers()
        elif choice == '5':
            print("Exiting the program...")
            break
        else:
            print("Invalid choice! Please choose a valid option.")

        # Ask the user if they want to continue
        continue_choice = input("\nDo you want to continue? (yes/no): ").lower()
        if continue_choice != 'yes':
            print("Exiting the program...")
            break


# Run the program
if __name__ == "__main__":
    main()
