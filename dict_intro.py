vehicles = {
    'dream': 'Honda 250T',
    'er5': 'Kawasaki ER5',
    'can-am': 'Bombardier Can-Am 250',
    'virago': 'Yamaha XV250',
    'tenere': 'Yamaha XT650',
    'jimny': 'Suzuki Jimny 1.5',
    'fiesta': 'Ford Fiesta Ghia 1.4',
    'roadster': 'Triumph Street Triple',
}

vehicles["starfighter"] = "Lockheed F-104"
vehicles["learjet"] = "Bombardier Learjet 75"
vehicles["toy"] = "glider"

# upgrading the virago:
vehicles["virago"] = "Yamaha XV535"

del vehicles["starfighter"]
# del vehicles["f1"]
result = vehicles.pop("f1", "Instead of an error gimme this")  # the None
# makes sure there will be no error, even if the key does not exist!
print(result)
print()

bike = vehicles.pop("tenere", "not present")
# commuter = vehicles['virago']
# print(commuter)
#
# learner = vehicles.get("er5")  # the advantage is that GET will not
# crash the program but return None, when the key is not found;
# However, indexing is faster!
# print(learner)

# when you iterate over a dictionary, you iterate over the keys:
for key in vehicles:
    print(key)

print()

# for key in vehicles:
#     print(key, vehicles[key], sep=", ")
# more efficient way:
for key, value in vehicles.items():
    print(key, value, sep=", ")
