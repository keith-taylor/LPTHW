ten_things = "Apple IcanIcan't Crows Telephone HotSugar Magic"
print("Wait there are not ten strings in that list. Let's fix that. ")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Bananna", "Girl", "Boy"]

while len(stuff) < 10:
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items in there now. ")
    
print("There we go. ", stuff)

print("\nLet's do some things with stuff.")

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(' '.join(stuff))
print('--'.join(stuff[2:5]))

