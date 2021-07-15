file = open('myfile.txt', 'rt')

for line in file:
    print('- ', line)

file.close()
