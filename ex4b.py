cars = 100
space_in_a_car =  4
drivers = 35
passengers = 99
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * (space_in_a_car - drivers) 
average_passengers_per_car = passengers / cars_driven

print(f"There are {cars} cars available. ")
print(f"There are only {drivers} drivers available. ")
print(f"There will be {cars_not_driven} empty cars today. ")
print(f"We can transprot {int(carpool_capacity)} people today. ")
print(f"We have {passengers} people to carpool today. ")
print(f"We need to put about {int(average_passengers_per_car)} people in each car. ")
