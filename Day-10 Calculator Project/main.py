def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return  n1 - n2

def multiply(n1, n2):
    return  n1 * n2

def divide(n1, n2):
    return  n1/n2

maths_dict = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

result = None
continue_loop = True
while continue_loop:
    if result is None:
        user_input1 = float(input("Enter your first number: "))
    else:
        user_input1 = result

    for key in maths_dict:
        print(f"{key}")

    user_sign = input("Pick an operation: ").strip()
    if user_sign not in maths_dict:
        print("Invalid operation! Let's try again.")
        continue

    user_input2 = float(input("Enter the second number: "))

    if user_sign in maths_dict:
        result = maths_dict[user_sign](user_input1, user_input2)
        print(f"{user_input1} {user_sign} {user_input2} = {result}")

        choice = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation or type 'e' to exit: ")
        if choice == "y":
            continue
        elif choice == "n":
            result = None
        else:
            break

