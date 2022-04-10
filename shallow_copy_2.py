lion_list = ["scary", "big", "cat"]
elephant_list = ["big", "grey", "wrinkled"]
teddy_list = ["cuddly", "stuffed"]

animals = {
	"lion": lion_list,
	"elephant": elephant_list,
	"teddy": teddy_list,
}

# things = animals.copy()  # create a new dict as a shallow copy
things = {
	"lion": lion_list,
	"elephant": elephant_list,
	"teddy": teddy_list,
}

print(things["teddy"])
print(animals["teddy"])

print()

# things["teddy"].append("toy")
teddy_list.append("toy")  # does the same as above
animals["teddy"].append("added via `animals`")
things["teddy"].append("added via `things`")
print(things["teddy"])
print(animals["teddy"])
print(teddy_list)
