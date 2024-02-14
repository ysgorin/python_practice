# 1 American mile = 1609.344 metres
# 1 American mile = 1.609344 kilometers
# 1 American gallon = 3.785411784 litres

def liters_100km_to_miles_gallon(liters):
    liters_per_one_km = liters/100
    km_per_liter = 1/liters_per_one_km
    miles_per_gallon = ((1/1.609344)/(1/(3.785411784))) * km_per_liter
    return miles_per_gallon

def miles_gallon_to_liters_100km(miles):
    km_per_liter = ((1.609344)/(3.785411784)) * miles
    liters_per_one_km = 1/km_per_liter
    liters_per_hundred_km = liters_per_one_km * 100
    return liters_per_hundred_km

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))