#!/usr/bin/env python3
# Class Lab
# Michael Dougherty and Rasaki Solebo
# Mar 7 2023
from datetime import date

# Write a file called 'Dougherty-Solebo-ClassLab.txt'
filename = "Dougherty-Solebo-ClassLab.txt"

aFile = open(filename, "w")

name = "Michael Dougherty & Rasaki Solebo"
className = "CIS 245 - Principles of Software Development"

aFile.write(f"{name}\n{className}\n{date.today()}\n")
aFile.close()

# Open the file and print the contents
bFile = open(filename)
for line in bFile:
    print(line, end='')
