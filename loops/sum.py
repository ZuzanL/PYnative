# Write a program to accept a number from a user and calculate 
# the sum of all numbers from 1 to a given number

import sys
cislo = int(sys.argv[1])
c = 0
suma = 0

while c <= cislo:
    suma += c
    c += 1
print(suma)
