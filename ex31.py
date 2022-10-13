print("""You enter a dark room with two doors.
      
Do you go throughdoor 1, or door 2?""")

prompt_message = "Please enter either 1 or 2 and hit Return."
print(prompt_message)

prompt = ":> "
door_choice = input(prompt)

if door_choice == "1":
    print("There's a giant bear here eating a cheese cake. ")
    print("What do you want to do?")
    print("1. Take the cheese cake?")
    print("2. Scream at the bear?")
    print(prompt_message)

    bear_choice = input(prompt)

    if bear_choice == "1":
        print("The bear eats your face clean off your skull. Too bad.")
    elif bear_choice == "2":
        print("The bears chews you legs off. Condolences. ")
    else:
        print(f"Well, doing {bear_choice} is probably better.")
        print("The bear slopes off mumbling something about a prior engagement.")

elif door_choice == "2":
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.")
        print("Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!")