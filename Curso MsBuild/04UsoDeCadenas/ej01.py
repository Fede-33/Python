# Considerando el siguiente texto:

# Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. 
# On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature of the Moon is 127 C.

# Almacénelo en una variable y luego sepárelo en oraciones, almacenándolas en otra variable como una lista. E imprímalas en pantalla:

text = """Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. 
On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature of the Moon is 127 C."""

orac = text.split('. ')
print(orac)

# Encuentre e imprima las oraciones que mencionen la palabra "temperature"

for temp in orac:
    if 'temperature' in temp:
        print(temp)
