#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#task 2 calculator
import math

# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

# Function to calculate the square root of a number
def square_root(x):
    if x < 0:
        return "Invalid input. Cannot calculate the square root of a negative number."
    return math.sqrt(x)

# Function to calculate the exponentiation of a number
def exponentiate(x, y):
    return x ** y

# Function to calculate the modulus of two numbers
def modulus(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x % y

# Main calculator function
def calculator():
    print("Welcome to the Calculator!")

    while True:
        print("Options:")
        print("Enter 'add' for addition")
        print("Enter 'subtract' for subtraction")
        print("Enter 'multiply' for multiplication")
        print("Enter 'divide' for division")
        print("Enter 'sqrt' for square root")
        print("Enter 'exponentiate' for exponentiation")
        print("Enter 'modulus' for modulus")
        print("Enter 'quit' to end the program")

        user_input = input(": ")

        if user_input == "quit":
            print("Thank you for using the calculator. Goodbye!")
            break
        elif user_input in ("add", "subtract", "multiply", "divide", "sqrt", "exponentiate", "modulus"):
            if user_input == "sqrt" or user_input == "exponentiate" or user_input == "modulus":
                num = float(input("Enter a number: "))
                if user_input == "sqrt":
                    result = square_root(num)
                elif user_input == "exponentiate":
                    exp = float(input("Enter an exponent: "))
                    result = exponentiate(num, exp)
                elif user_input == "modulus":
                    num2 = float(input("Enter another number: "))
                    result = modulus(num, num2)
            else:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))

                if user_input == "add":
                    result = add(num1, num2)
                elif user_input == "subtract":
                    result = subtract(num1, num2)
                elif user_input == "multiply":
                    result = multiply(num1, num2)
                elif user_input == "divide":
                    result = divide(num1, num2)

            print("Result:", result)
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    calculator()


# In[ ]:




