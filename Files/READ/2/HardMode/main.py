def get_planets_list_from_file(filename='planets.txt'):
    file = open(filename, 'rt', encoding='utf-8')
    planets = []

    for line in file:
        line_planets = line.rstrip().split(',')
        for brute_planet in line_planets:
            planets.append(brute_planet.strip())

    file.close()
    return planets


print(get_planets_list_from_file())
