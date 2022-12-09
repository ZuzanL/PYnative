# Write a program to print multiplication table of a given number
import sys
cislo = int(sys.argv[1])
c = 1
nasobky = 1

while c <= 10:
    nasobky = nasobky * cislo
    print(nasobky)
    nasobky = c + 1
    c += 1