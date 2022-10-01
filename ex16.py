from sys import argv

script, filename = argv

print(f"We're going to erase {filename}. ")
print("If you don't want that hit CTRL-C (^C). ")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye. ")
target.truncate()
print(f"The file is now truncated: ") 
#print(target.read())

print("Now I'm going to ask you for three lines. ")
line_1 = input("line 1: ")
line_2 = input("line 2: ")
line_3 = input("line 3: ")

print("I'm going to write these lines to the file. ")

target.write(line_1)
target.write("\n")
target.write(line_2)
target.write("\n")
target.write(line_3)
target.write("\n") 

print(f"Lines added, m,lud: ") 


print("And now to bed. ")
target.close() 








