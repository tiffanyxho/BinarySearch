import csv
import string
import math

# f is a file
f = open('countries.csv')

data = f.read()
countries = data.split("\n")

length = len(countries)
start = 0
end = length - 1
middle = (end - start)//2
searching = True

#print (countries)
search = input("What country do you want to search for? ")


while searching:
    if start == end:
        searching = False
        if countries[start] == search:
            print("right")
        else:
            print("no")
    elif start != end:
        if countries[middle] > search:
            print("lower half")
            end = middle - 1
            middle = (end - start)//2
            middle = end - middle
        elif countries[middle] < search:
            print("upper half")
            start = middle + 1
            middle = (end - start)//2
            middle = middle + start
        elif countries[middle] == search:
            print("Your country is in the directory.")
            searching = False

# 5, 6, 9, 10, 11, 12, 13-15, 23
