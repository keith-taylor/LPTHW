def print_two(*args):
    print(len(args))
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")
    
def print_two_2(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

def print_one(arg1):
    print(f"arg1: {arg1}")

def print_none():
    print("I got nuttin'.")

print_two("Keith", "Hello")
print_two_2("Kahki", "Kind")
print_one("Kettle")
print_none()