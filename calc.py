import math

print("Welcome to the Calculator App")
print("The following operations are available: + - / *")
print("Please separate entries with a space. Ex: Use 1 + 2 instead of 1+2")
print("Type \"Q\" to quit the program.")

result = None
op = None
first = True

while(True):
    calc = input().strip().split()
    if calc[0].lower() == "q":
        break

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
        if result % 1 == 0:
            print("= ", math.trunc(result))
        else:
            print("= {0:.2f}".format(result))

print("Goodbye :)")