#!/usr/local/bin/python3
# Made by @swisscoding on Instagram
# Follow now and share!

from colored import stylize, fg

# decoration
print(stylize("\n---- | Get maximum travel distance | ----\n", fg("red")))

# user interaction
fuel = float(input("Fuel in the tank (> 1): "))
fuel_usage = float(input("Fuel usage liters/100km (> 1): "))
passengers = int(input("Amount of passengers: "))
air_con = True if input("Air condiditoner (on/off): ").lower() == "on" else False

# function
def distance(liters, liters_per_100km, persons, conditiner):
    if liters <= 1 or liters_per_100km <= 1 or passengers < 0:
        return "Invalid Input"
    if persons == 0 and not conditiner:
        return round(100 / liters_per_100km * liters, 2)
    elif persons == 0 and conditiner:
        return round(100 / (liters_per_100km + liters_per_100km / 100 * 10) * liters, 2)
    elif not conditiner:
        return round(100 / (liters_per_100km + liters_per_100km / 100 * 5 * persons) * liters, 2)
    else:
        total_fuel_usage = (liters_per_100km + liters_per_100km / 100 * 5 * persons)
        return round(100 / (total_fuel_usage + total_fuel_usage / 100 * 10) * liters, 2)

max_distance = stylize(distance(fuel, fuel_usage, passengers, air_con), fg("green"))
print(f"\nWith the given conditions the maximum\ntravel distance is {max_distance} km.\n")
