travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇



def add_new_country(new_country, new_times, new_cities):
    new_country_dict = {}
    new_country_dict["country"] = new_country
    new_country_dict["visits"] = new_times
    new_country_dict["cities"] = new_cities
    travel_log.append(new_country_dict)
    

#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)



