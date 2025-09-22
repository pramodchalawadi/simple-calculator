# simple-calculator
This project is a user-friendly console-based calculator written in Python that performs basic arithmetic operations using the input() method. It's designed with a focus on user experience, error handling, and clean code organization through modular function design.


##  Features

- **Basic Arithmetic Operations**: Addition (+), Subtraction (-), Multiplication (*), Division (/)
- **Input Validation**: Ensures valid numbers and operators are entered
- **Error Handling**: Gracefully handles division by zero and invalid inputs
- **Continuous Operation**: Perform multiple calculations in one session
- **User-Friendly Interface**: Clean prompts with emoji indicators and clear formatting
- **Smart Number Formatting**: Displays whole numbers without unnecessary decimal places
- **Flexible Input**: Accepts various confirmation responses (yes, y, yeah, yep)

##  Installation

### Prerequisites

- Python 3.x installed on your system
- No additional libraries required (uses only built-in Python functions)

### Setup

1. **Clone or download the repository**
   ```bash
   git clone https://github.com/yourusername/simple-python-calculator.git
   cd simple-python-calculator
   ```

2. **Run the calculator**
   ```bash
   python calculator.py
   ```

##  Usage

### Basic Operation

1. **Start the program**
   ```bash
   python calculator.py
   ```

2. **Follow the prompts**
   - Enter your first number
   - Choose an operator (+, -, *, /)
   - Enter your second number
   - View the result

3. **Continue or Exit**
   - Type "yes" or "y" to perform another calculation
   - Type "no" or "n" to exit the program

### Example Session

```
 Welcome to Python Simple Calculator!
========================================

Let's do some calculations! 
Enter first number: 15
Enter operator (+, -, *, /): *
Enter second number: 4

 Result: 15.0 * 4.0 = 60

----------------------------------------
Do you want to perform another calculation? (yes/no): yes
========================================

Let's do some calculations! 
Enter first number: 100
Enter operator (+, -, *, /): /
Enter second number: 0

 Error: Cannot divide by zero!

----------------------------------------
Do you want to perform another calculation? (yes/no): no

Thank you for using the calculator! Have a great day!
```

##  Code Structure

The calculator is built with a modular approach using four main functions:

### Functions Overview

| Function                            | Purpose              | Description                                      |
|-------------------------------------|----------------------|--------------------------------------------------|
| `get_number(prompt)`                | Input Validation     | Safely gets a valid number from user input       |
| `get_operator()`                    | Operator Validation  | Ensures user enters a valid operator             |
| `calculate(num1, operator, num2)`   | Calculation Engine   | Performs arithmetic operations safely            |
| `main()`                             | Program Control     | Manages the main program flow and user interaction |

### Architecture Benefits

- **Modular Design**: Easy to maintain and extend
- **Error Isolation**: Problems are contained within specific functions
- **Reusability**: Functions can be easily reused or modified
- **Testing**: Individual functions can be tested independently

##  Examples

### Supported Operations

```python
# Addition
15 + 25 = 40

# Subtraction  
50 - 30 = 20

# Multiplication
7 * 8 = 56

# Division
100 / 4 = 25
```

### Input Validation Examples

```
# Invalid Number Input
Enter first number: abc
 Please enter a valid number!
Enter first number: 15

# Invalid Operator Input
Enter operator (+, -, *, /): %
 Please enter a valid operator (+, -, *, /)
Enter operator (+, -, *, /): +
```

##  Error Handling

The calculator includes comprehensive error handling:

### Input Validation
- **Non-numeric Input**: Prompts user to enter valid numbers
- **Invalid Operators**: Ensures only +, -, *, / are accepted
- **Whitespace Handling**: Automatically trims extra spaces

### Mathematical Errors
- **Division by Zero**: Detects and prevents division by zero operations
- **Overflow Protection**: Handles very large numbers gracefully

### User Experience
- **Clear Error Messages**: Friendly, descriptive error notifications
- **Recovery Options**: Users can retry without restarting the program
- **Graceful Degradation**: Program continues running despite errors

##  Customization

### Adding New Operations

To add new operations, modify the `get_operator()` and `calculate()` functions:

```python
def get_operator():
    while True:
        operator = input("Enter operator (+, -, *, /, %, **): ").strip()
        if operator in ['+', '-', '*', '/', '%', '**']:
            return operator
        print(" Please enter a valid operator")

def calculate(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            return None
        return num1 / num2
    elif operator == '%':
        return num1 % num2
    elif operator == '**':
        return num1 ** num2
```

### Styling Customization

Modify the emoji and formatting characters to match your preference:

```python
# Change emojis and separators
print(" Custom Calculator!")  # Different emoji
print("*" * 40)                 # Different separator
```

##  Testing

### Manual Testing Scenarios

Test the following cases to ensure proper functionality:

1. **Normal Operations**
   - Test all four basic operations
   - Use both integers and decimals
   - Verify correct results

2. **Error Cases**
   - Division by zero
   - Invalid number inputs (letters, symbols)
   - Invalid operators
   - Empty inputs

3. **Edge Cases**
   - Very large numbers
   - Very small decimal numbers
   - Negative numbers



**Made with  and Python** | **Happy Calculating! **
