text = 'Jazz, musical form, often improvisational, developed by African Americans and influenced by both European harmonic structure and African rhythms. It was developed partially from ragtime and blues and is often characterized by syncopated rhythms, polyphonic ensemble playing, varying degrees of improvisation, often deliberate deviations of pitch, and the use of original timbres.'

letters_counts = {}

for letter in text:
    if letter in letters_counts:
        letters_counts[letter] += 1
    else:
        letters_counts[letter] = 1

for letter in letters_counts:
    print(letter, ':', letters_counts[letter])
