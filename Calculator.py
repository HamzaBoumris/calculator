print("Simple Calculator")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Choose operation (1-4): ")
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if choice == '1':
    print(f"Result: {a + b}")
elif choice == '2':
    print(f"Result: {a - b}")
elif choice == '3':
    print(f"Result: {a * b}")
elif choice == '4':
    if b != 0:
        print(f"Result: {a / b}")
    else:
        print("Error: Cannot divide by zero.")
else:
    print("Invalid choice.")
