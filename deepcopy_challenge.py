from contents import recipes


def my_deepcopy(dictio: dict) -> dict:
    """
    Create a deepcopy of a `dictio` down one level

    :param dictio: dictionary
    :return: copy of the dictionary
    """
    new_dict = {}
    for key, value in dictio.items():
        new_value = value.copy()
        new_dict[key] = new_value
    return new_dict


recipes_copy = my_deepcopy(recipes)
recipes_copy["Butter chicken"]["ginger"] = 300
print(recipes_copy["Butter chicken"]["ginger"])
print(recipes["Butter chicken"]["ginger"])
# a_list = ["just", "for good measure"]
# a_dict = {"a": 0, "b": 1}
# testing_dict = {
#     1: "hello",
#     2: a_dict,
#     3: a_list,
# }
#
# receiver = my_deepcopy(testing_dict)
# a_list.append("PUNKT")
# a_dict["c"] = 2
# a_dict["a"] = 100
# print(testing_dict)
# print(receiver)