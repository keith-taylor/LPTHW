from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)

def print_a_line(line_numb, f):
    print(line_numb, f.readline())

current_file = open(input_file)

print("Fist let's print the whole file: \n")

print_all(current_file)

print("Now let's rewind, be kind: ")

rewind(current_file)

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
