a = input("Enter your first digit: ")
operator = input("Enter your operator: ")
b = input("Enter your second digit: ")

if operator == "+":
    print(int(a) + int(b))

elif operator == "-":
    print(int(a)-int(b))

elif operator == "/":
    print(int(a)/int(b))

elif operator == "*":
    print(int(a)*int(b))

elif operator == "%":
    print(int(a)%int(b))

elif operator == "//":
    print(int(a)//int(b))

else:
    print("Invalid Values")