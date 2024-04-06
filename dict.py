vehicles = {
    'dream' : 'Honda 250T',
    'roadster' : 'BMW R1100',
    'er5': 'Kawasaki ER5',
    'can-am' : 'Bombardier Can-Am 250',
    'virago' : 'Yamaha XV250',
    'tenere' : 'Yamaha HT650',
    'jimny' : 'Suzuki Jimny 1.5',
    'fiesta' : 'Ford Fiesta Ghia 1.4',
    'roadster' : 'Triumph Street Triple',
}


vehicles["starfighter"] = "Lockhead F-104"
vehicles["learjet"] = "Bombardier Learjet 75"
vehicles["toy"] = "glider"

#Upgrade the Virago
vehicles["virago"] = "Yamaha XV535"

del vehicles["starfighter"]
result = vehicles.pop("f1","You wish!Sell the Learjet and you might afford a racing car.")
print(result)
plane = vehicles.pop("learjet")
print(plane)

bike = vehicles.pop("tenere", "not present")
print(bike)
print()

#for key in vehicles:
#    print(key, vehicles[key], sep=", ")

for key,value in vehicles.items():
    print(key, value, sep=", ")

