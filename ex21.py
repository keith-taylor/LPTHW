from re import A


def add(a, b):
    print(f"Adding {a} and {b}")
    return a + b

def subtract(a, b):
    print(f"Subtracting {b} from {a}")
    return a - b

def multiply(a, b):
    print(f"Multiplying {a} and {b}")
    return a * b

def divide(a, b):
    print(f"Dividing {a} by {b}")
    return a / b

print("Let's do some math!")

print("What is your age? ")
age = int(input())

age = add((age),5)
height = subtract(78,4)
weight = multiply(90,2)
iq = divide (100,2)

print(f"Age: {age}, height: {height}, weight: {weight}, IQ: {iq}. ")

print("Here is a puzzle!") 
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print(f"That becomes: {what}. Can you do it by hand? ")
 
 
