def get_planets_list_from_file(filename='planets.txt'):
    file = open(filename, 'rt', encoding='utf-8')
    planets = []

    for line in file:
        line_planets = line.rstrip().split(', ')
        planets.extend(line_planets)

    file.close()
    return planets


print(get_planets_list_from_file())
