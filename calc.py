print("Welcome to the Calculator App")
print("The following operations are available: + - / *")
print("Please separate entries with a space. Ex: Use 1 + 2 instead of 1+2")
print("Type \"Q\" to quit the program.")

result = None

while(True):
    result = None
    calc = input().strip().split()
    if calc[0].lower() == "q":
        break

    op = None
    for item in calc:
        if item.isnumeric():
            if result is None:
                result = int(item)
            else:
                num = int(item)
                if op == "+":
                    result += num
                elif op == "-":
                    result -= num
                elif op == "*":
                    result *= num
                elif op == "/":
                    result /= num
                else:
                    print("Bad Input.")
                    result = None
                    break
        elif item.isalpha():
            print("Bad Input")
            result = None
            break
        else:
            op = item

    if result is not None:
        print("= ", result)

print("Goodbye :)")