d = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    "iv": "four"
}

pantry_items = ['chicken', 'spam', 'egg', 'bread', 'lemon']

v = d.values()
print(v)
# dynamic view window!!!
d[10] = "ten"
print(v)

print("four" in v)
print("eleven" in v)

keys = list(d.keys())
values = list(v)  # => list(d.values())
if "four" in values:
    index = values.index("four")
    key = keys[index]
    print(f"{d[key]} was found with the key {key}")

print()

for key, value in d.items():
    if value == "four":
        print(f"{d[key]} was found with the key {key}")

# Core for the dict `update` methods lecture
# **********************************************
# d2 = {
#     7: "lucky seven",
#     10: "ten",
#     3: "this is the new three",
# }
#
# d.update(d2)
# # update takes the key-value pairs passed to it to update a dictionary
# # update(other) is equivalent to
# # d |= other  <-- augmented assignment
# for key, value in d.items():
#     print(key, value)
#
# print()
#
# d.update(enumerate(pantry_items))
# for key, value in d.items():
#     print(key, value)


# Code for "The remaining `dict`  methods lecture
# ******************************************************
# new_dict = dict.fromkeys(pantry_items, 0)
# print(new_dict)
#
# keys = d.keys()
# print(keys)
#
# for item in d:
#     # same as  item in d.keys():
#     print(item)
