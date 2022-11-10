import os

os.chdir("dir_1")

# Ex 1
number = ""
number_1 = 0
with open("updated.txt") as txt_file:
    #     for count, line in enumerate(txt_file):
    #         pass
    # print(count + 1)

    first_file = txt_file.readline()
    first_file_ = txt_file.readline()

    for path in first_file:
        for digits in path:
            if digits.isdigit():
                # number += digits
                number_1 += 1
print(first_file, first_file_)

# Ex 2

num_1 = 0
with open("updated.txt", "r") as text_1:
    for line in text_1:
        for number in line:
            if number.isdigit():
                num_1 += 1
print("The number of digits in file is: ", num_1)


# Ex 3

list_1 = []
with open("updated.txt", "r") as text_2:
    text = text_2.read().split()
    for line in text:
        if line.startswith("<<") and line.endswith(">>"):
            list_1.append(line)

print(list_1)


# Ex 4
new_file = ""
with open("updated.txt") as with_d, open("updated_2.txt", "a") as without_d:
    # first_file = with_d.read()

    for lines in with_d:
        for letters in lines:
            if not letters.isdigit():
                new_file += letters

    without_d.write(new_file)
