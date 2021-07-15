file = open('myfile.txt', 'rt')

text = file.readline()
print(text)
text = file.read()
print(text)

file.close()
