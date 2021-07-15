def get_planets_list_from_file(filename='planets.txt'):
    file = open(filename, 'rt', encoding='utf-8')
    planets = []

    for line in file:
        line_planets = line.rstrip().split(', ')
        for planet in line_planets:
            planets.append(planet)

    file.close()
    return planets


print(get_planets_list_from_file())
