my_text = open(r"C:\Users\thepa\bolinha-stuff\just_files\vol_as_is_t.txt", 'r').readlines()

for index in range(len(my_text)):
    if "Î”" in my_text[index]:
        to_be_replaced = my_text[index][my_text[index].find("Î”") - 1: my_text[index].find("]") + 1]
        my_text[index] = my_text[index].replace(to_be_replaced, "0")
    elif my_text[index] == "\\n":
        my_text[index] = ""
    print(my_text[index], sep="")

output_file = open(r"C:\Users\thepa\bolinha-stuff\just_files\vol_out.txt", 'w')
print(my_text[0], file=output_file, sep="")
output_file = open(r"C:\Users\thepa\bolinha-stuff\just_files\vol_out.txt", 'a')
for i in range(1, len(my_text)):
    print(my_text[i], file=output_file, sep="")
