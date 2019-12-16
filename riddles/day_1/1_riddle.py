import math

filepath = open('1_module_mass', 'r')
totalFuel = 0


def calculateFuel(mass):
    fuel = (math.floor(mass/3))-2
    global totalFuel
    totalFuel += fuel
    print(totalFuel)

    # Part 2 of day 1
    if (math.floor(fuel/3))-2 > 0:
        calculateFuel(fuel)


for x in filepath:
    calculateFuel(int(x))

