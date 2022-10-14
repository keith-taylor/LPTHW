states = {
    'Oergon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michegan': 'MI',
    'Illinois': 'IL',
    'Washington': 'WA',
    'Pennsylvania': 'PA'
}

cities = {
    'CA': ['San Franciso', 'Los Angeles', 'Los Alamos', 'Sacramento'],
    'MI': ["Detroit"], 
    'FL': ['Jacksonville'],
    'NY': ['New York', 'Albany'],
    'OR': ['Portland'],
    'IL': ['Chicago'],
    'WA': ['Seatle'],
    'PA': ['Philadelphia']
}


#print(cities)

# print('-' * 10)
# print("NY State has: ", cities['NY'])
# print("OR State has: ", cities['OR'])

# print('-' * 10)
# print("Michegan's abbreviation is: ", states['Michegan'])
# print("Florida's abbreviation is: ", states['Florida'])

# print('-' * 10)
# print("Michegan has: ", cities[states['Michegan']])
# print("Florida has: ", cities[states['Florida']])


for each_state in states:
    cities_list = []
    for each_city in cities[states[each_state]]:
        cities_list.append(each_city)
    print(f"These are the listed cities for {each_state} state: {', '.join(cities_list)}. ")