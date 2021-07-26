"""
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])

You've visited Russia 2 times.
You've been to Moscow and Saint Petersburg.
"""

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris","Lille","Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin","Hamburg","Stuttgart"]
},
]
#TODO: Write the function that will allow new countries
#to be added to the travel_log.
def add_new_country(country_visited,times_visited,cities_visited):
    new_country = {}
    #new_country[key] = value
    new_country["country"] = country_visited
    new_country["visits"] = times_visited
    new_country["cities"] = cities_visited
    travel_log.append(new_country)

  # way_2
  # new_country = {"country":country_visited,"visits":times_visited,"cities":cities_visited}
  # travel_log.append(new_country)

#Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)