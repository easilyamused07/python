#11-1

def city_and_country(city,country,population=''):
    
    if population:
        formatted = city.title() + ", " + country.title() + " - " + \
            "population " + str(population)
    else:
        formatted = city.title() + ", " + country.title()
    return formatted
