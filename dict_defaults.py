from contents_quantities import pantry

chicken_quantity = pantry.setdefault("chicken", 0)
# if the key is already in the dictionary, it will just retrieve its value!
print(f"chicken: {chicken_quantity}")

beans_quantity = pantry.setdefault("beans", 0)
print(f"beans: {beans_quantity}")
# the setdefault method adds the key to the dict if it doesn't exist!
# get does not do that
ketchup_quantity = pantry.get("ketchup", 0)
print(f"ketchup: {ketchup_quantity}")

z_quantity = pantry.setdefault("zucchini", "eight")
print(f"zucchini: {z_quantity}")
print()
print("`pantry` now contains...")

for key, value in sorted(pantry.items()):
    print(key, value)