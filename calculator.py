from calculations import calculate
answer = None
work = True
while work:
    first_number = input("Enter first number: ")
    available_operations = "+ - * / s(square), e(exponentiation), %(modulo)"
    print(f"Available operations: {available_operations}")
    operation = input("Choose operation: ")  # +, -, *, /, %, s, e
    result = None
    if operation == 's':
        second_number = first_number
    else:
        second_number = input("Enter second number: ")
    if first_number.lstrip("-").replace(".", "", 1).isdigit() \
            and second_number.lstrip("-").replace(".", "", 1).isdigit():
        first_number = float(first_number)
        second_number = float(second_number)
        if operation == "/" and second_number == 0:
            result = "You cannot divide by 0"
        else:
            result = calculate(first_number, second_number, operation)
    else:
        result = "Something went wrong"

    if operation == "/" and second_number != 0:
        print(f'result = {result:.2f}')
    else:
        print(f"Result: {result}")
    answer = (input('do you want to continue? Y/no ')).upper()
    if answer != 'Y':
        break
