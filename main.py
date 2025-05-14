def calculate(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Ката"
    else:
        return "Колдоого алынбаган амал."


while True:
    user_input = input(" киргизиңиз ").lower()
    if user_input == 'чыгуу':
        print(" аяктоо.")
        break

    parts = user_input.split()
    if len(parts) != 3:
        print("Туура эмес.")
        continue

    try:
        num1 = float(parts[0])
        operation = parts[1]
        num2 = float(parts[2])
        result = calculate(num1, num2, operation)
        print(f"Натыйжасы: {result}")
    except ValueError:
        print("Ката.")
    except Exception as e:
        print(f"Ката кетти: {e}")

