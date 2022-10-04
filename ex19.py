import math

def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses! ")
    print(f"You have {boxes_of_crackers} cwackers! ")
    print(f"That's enough for a party.")
    print(f"Get a blanket man!\n")
    
print("We can just give the function the numbers directly: ")
cheese_and_crackers(20, 30)

print("Or, we can just use a variable from our script: ")
amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do math inside too: ")
cheese_and_crackers(10+12, 34-21)

print("And we can combine the two, variable and math: ")
cheese_and_crackers(10+12, amount_of_crackers)
    
    
def things_in_the_attic(boxes, old_pictures, rugs, photo_albums, xmas_trees):
    print(f"You have exaclty {boxes} boxes in the attic. ")
    print(f"You have exaclty {old_pictures} old pictures in the attic. ")
    print(f"You have exaclty {rugs} rugs in the attic. ")
    print(f"You have exaclty {photo_albums} photo albums in the attic. ")
    print(f"You have exaclty {xmas_trees} xmas trees in the attic. ")
    print(f"That's a total of {sum([boxes, old_pictures, rugs, photo_albums, xmas_trees])} things in your atttic. ")
    print("Time for a clear out man!") 
    
old_pictures_in_the_attic = 5
rugs_in_the_attic = 2
things_in_the_attic(12+2, old_pictures_in_the_attic+1, rugs_in_the_attic, (int(math.sqrt(9))), 1)
    