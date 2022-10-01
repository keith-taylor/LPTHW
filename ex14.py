from sys import argv
script, user_name, hat_type = argv

prompt = ':: '

print(f"Hi {user_name}, I'm the {script} script. ")
print(f"I like that {hat_type} you're wearing. Very stylish. ")

print(f"Do you like me {user_name}? ")
likes = input(prompt) 

print(f"Where do you live {user_name}? ")
lives = input(prompt)

print("What kind of computer do you have? ")
computer = input(prompt)

print(f"""
      Alright, so you said '{likes}' about liking me.
      You live in {lives}. I'm not sure where that is.
      And you have a {computer} computer. Nice.
      """)

