import sys

words = {} 
vert = {}

def first_letter(word, diction):
    for count, x in enumerate(word):
        if count in diction:
            diction[count] = diction[count] + x
        elif count not in diction:
            diction[count] = x


for x in sys.stdin:
    x = list(x.strip())
    first_letter(x, words)

lines = sorted(words.values(), key=str.lower)

for x in lines:
    x = list(x.strip())
    first_letter(x, vert)

for count, x in enumerate(vert):
    if count in vert:
        print(vert[count])
