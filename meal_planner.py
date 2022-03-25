from contents_quantities import pantry, recipes


def add_shopping_item(data: dict, item: str, amount: int) -> None:
    """Add `amount` to an `item`

    :param data:
    :param item:
    :param amount:
    :return:
    """
    data[item] = data.setdefault(item, 0) + amount


display_dict = {}
for index, key in enumerate(recipes):
    display_dict[str(index + 1)] = key

while True:
    # display recipes we know how to cook
    print("\nPlease choose your recipe")
    print("-------------------------")
    for key, value in display_dict.items():
        print(f"{key} - {value}")

    choice = input(": ")

    if choice == "0":
        break
    elif choice in display_dict:
        selected_item = display_dict[choice]
        print(f"You have selected {selected_item}")
        print("Checking ingredients...")
        ingredients = recipes[selected_item]
        print(ingredients)
        for food_item, required_qty in ingredients.items():
            # get will check if we have at all in pantry or not
            # and return 0 instead of ValueError if not there
            quantity_in_pantry = pantry.get(food_item, 0)
            if required_qty <= quantity_in_pantry:
                print(f"\t{food_item} OK")
            else:
                quantity_to_buy = required_qty - quantity_in_pantry
                print(f"\tYou need to buy {quantity_to_buy} of {food_item}")