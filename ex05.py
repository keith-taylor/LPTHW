name = "Keith S. Taylor esq"
age = 35 # this is a lie
height = 75 # inches
weight = 198 # lbs
eyes = 'brown'
teeth = "white" #ish
hair = 'brown'

converted_height_cm  = height * 2.54
converted_weight_kg = weight / 2.2

print(f"Let's talk about {name}. ")
print(f"I am {int(converted_height_cm)} cm tall. ")
print(f"I am {converted_weight_kg:.1f} kg in heavy. ")
print("I could do with losing a little I guess. ")
print(f"I have {eyes} eyes and {hair} hair. ")

total = age + height + weight 
print(f"If I add my stats I get: {total}. ")
