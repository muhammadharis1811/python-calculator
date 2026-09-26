def calculator():
    print("===== Simple Calculator =====")
    print("Enter 'q' to quit")

    while True:
        num1 = input("\nEnter first number: ")

        if num1.lower() == "q":
            print("Calculator closed.")
            break

        operator = input("Enter operator (+, -, *, /): ")

        num2 = input("Enter second number: ")

        try:
            num1 = float(num1)
            num2 = float(num2)

            if operator == "+":
                result = num1 + num2
            elif operator == "-":
                result = num1 - num2
            elif operator == "*":
                result = num1 * num2
            elif operator == "/":
                if num2 == 0:
                    print("Error: Cannot divide by zero.")
                    continue
                result = num1 / num2
            else:
                print("Invalid operator.")
                continue

            print("Result:", result)

        except ValueError:
            print("Please enter valid numbers.")


calculator()
