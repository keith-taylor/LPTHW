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


for each_state in states:
    if len(cities[states[each_state]]) == 1:
        print(f"There is only one city listed in {each_state} [{states[each_state]}]: {', '.join(cities[states[each_state]])}.  ")
        
    else:
        print(f"There are {len(cities[states[each_state]])} cities listed in {each_state} [{states[each_state]}]: {', '.join(cities[states[each_state]])}. ")



print("\n")

home_nations = {
    'Scotland': 'Sco',
    'England': 'Eng',
    'Wales': 'Wal',
    'Northern Ireland': 'NIr'
    }

uk_cities = {
    'Sco': ["Glasgow", "Edinburgh", "Aberdeen", "Stirling"], 
    'Eng': ["London", "Manchestor", "Birmingham", "Leeds"], 
    'Wal': ["Cardiff", "Swansea"], 
    'NIr': ["Belfast"]
}
for country in home_nations:
    if len(uk_cities[home_nations[country]]) == 1:
        print(f"There is only one city listed in {country}: {', '.join(uk_cities[home_nations[country]])}.  ")
        
    else:
        print(f"There are {len(uk_cities[home_nations[country]])} cities listed in {country}: {', '.join(uk_cities[home_nations[country]])}. ")

