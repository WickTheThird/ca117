#!/usr/bin/env pytho3

import sys
words = {'0': 'zero', '1': 'one', '2': "two", '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine', '10': 'ten', '11': 'eleven', '12': 'twelve', '13': "thirteen", '14': 'fourteen', '15': 'fifteen', '16': 'sixteen', '17': 'seventeen', '18': 'eighteen', '19': 'nineteen'}
words_2 = {'20': 'twenty', '30': 'thirty', '40': "forty", '50': 'fifty', '60': 'sixty', '70': 'seventy', '80': 'eighty', '90': 'ninety', '100': 'one hundred'}

for x in sys.stdin:
    x = x.strip().split()
    a = []
    for y in x:
        if y in words:
            a.append(words[y])
        if y not in words and (y[0] + "0") in words_2 and y not in words_2:
            num = words_2[(y[0] + "0")] + "-" + words[(y[1])]
            a.append(num)
        if y in words_2 and y not in words:
            a.append(words_2[y])
    print(" ".join(a))
