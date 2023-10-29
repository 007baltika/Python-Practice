from math import *
for a in range(1, 151, 2):
    for b in range(1, 151, 2):
        for c in range(1, 151, 2):
            for d in range(1, 151, 2):
                for e in range(1, 151, 2):
                    if pow(a, 5) + pow(b, 5) + pow(c, 5) + pow(d, 5) == pow(e, 5):
                        print(a + b + c + d + e)
for a in range(2, 151, 2):
    for b in range(2, 151, 2):
        for c in range(2, 151, 2):
            for d in range(2, 151, 2):
                for e in range(2, 151, 2):
                    if pow(a, 5) + pow(b, 5) + pow(c, 5) + pow(d, 5) == pow(e, 5):
                        print(a + b + c + d + e)  