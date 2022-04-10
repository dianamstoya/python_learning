from contents import recipes


def my_deepcopy(d: dict) -> dict:
    new_dict = {}
    for key, value in d.items():
        new_value = value.copy()
        new_dict[key] = new_value

    return new_dict


recipes_copy = my_deepcopy(recipes)
recipes_copy["Butter chicken"]["ginger"] = 300
print(recipes_copy["Butter chicken"]["ginger"])
print(recipes["Butter chicken"]["ginger"])
