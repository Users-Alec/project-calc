# calculator project
import operations
import menu

def main():
    while True:
        menu.show_menu()
        choice = menu.get_choise()

        if choice == "0":
            print("Goodbye!")
            break

        if choice not in['1', '2', '3', '4']:
            print("invalid option")
            continue

        try:
            num1 = float(input("Enter your first number: "))
            num2 = float(input("Enter your second number: "))
        except ValueError:
            print("Enter valid numbers")
            continue

        if choice == "1":
            print("Reuslt:", operations.add(num1, num2))
        elif choice == "2":
            print("Result:", operations.substract(num1, num2))
        elif choice == "3":
            print("Result:", operations.multiply(num1, num2))
        elif choice == "4":
            print("Result:", operations.divide(num1, num2))


if __name__ == "__main__":
    main()
        