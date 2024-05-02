# Dictionary comprehension is a way to create a dictionary in Python using an expression. 
# this can replace for loops and certain lambda functions.

#----------------------------------------------------------------

# F means fahrenshite - the worst use of measuring temperature in existance.
# cities_in_F = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}

#----------------------------------------------------------------

# Now using a list with Celcius values like the majority of the world
# cities_in_C = {key: round((value-32)*(5/9)) for (key, value) in cities_in_F.items()}
# print(cities_in_C)

#----------------------------------------------------------------

# weather = {'New York': 'snowing', 'Boston': 'sunny', 'Los Angeles': 'sunny', 'Chicago': 'cloudy'}
# sunny_weather = {key: value for (key, value) in weather.items() if value == 'sunny'}
# print(sunny_weather)

#----------------------------------------------------------------

# cities = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
# desc_cities = {key: ('WARM' if value >= 50 else 'COLD') for (key, value) in cities.items()}
# print(desc_cities)

#----------------------------------------------------------------


def check_temp(value):
    if value >= 70:
        return 'HOT AS HELL, PLEASE STAY INSIDE! AND DRINK WATER! PS: THIS WEATHER CAN KILL YOU!'
    elif 69 >= value and value >= 40:
        return 'HOT STILL, DONT GO OUTSIDE!'
    else:
        return 'WARM OR COLD BUT WHO CARES!'
    
cities = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
desc_cities = {key: check_temp(value) for (key, value) in cities.items()}
print(desc_cities)