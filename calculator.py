# User-friendly Simple Calculator
def get_number(prompt):
    """Get a valid number from user input"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print(" Please enter a valid number!")

def get_operator():
    """Get a valid operator from user input"""
    while True:
        operator = input("Enter operator (+, -, *, /): ").strip()
        if operator in ['+', '-', '*', '/']:
            return operator
        print(" Please enter a valid operator (+, -, *, /)")

def calculate(num1, operator, num2):
    """Perform the calculation"""
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            return None  # Division by zero
        return num1 / num2

def main():
    """Main calculator function"""
    print(" Welcome to Python Simple Calculator!")
    print("=" * 40)
    
    while True:
        print("\nLet's do some calculations! ✨")
        
        # Get input from user
        num1 = get_number("Enter first number: ")
        operator = get_operator()
        num2 = get_number("Enter second number: ")
        
        # Calculate result
        result = calculate(num1, operator, num2)
        
        # Display result
        if result is None:
            print("\n Error: Cannot divide by zero!")
        else:
            # Format result nicely
            if result == int(result):
                result = int(result)  # Remove .0 for whole numbers
            
            print(f"\n Result: {num1} {operator} {num2} = {result}")
        
        # Ask if user wants to continue
        print("\n" + "-"*40)
        continue_calc = input("Do you want to perform another calculation? (yes/no): ").lower().strip()
        
        if continue_calc not in ['yes', 'y', 'yeah', 'yep']:
            print("\n Thank you for using the calculator! Have a great day!")
            break
        
        print("="*40)

# Run the calculator
if __name__ == "__main__":
    main()
