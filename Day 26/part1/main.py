# def fun(name):
#     with open(name, "r") as txt_file:
#         return txt_file.readlines()
#

# print(fun("file1.txt"))
# fist = [int(n.strip()) for n in fun("file1.txt")]
# second = [int(n.strip()) for n in fun("file2.txt")]
# print(fist)
# print(second)
#
# the_same = [n for n in fist if n in second]
# print(the_same)


# names = ["Alex", "Beth", "Richard", "Hanry"]
# import random
#
# names_with_scores = {i: random.randint(1, 100) for i in names}
#
# print({ keys:value for keys, value in names_with_scores.items() if value>59})

# print(names_with_scores)

# words = "К ней дамы подвигались ближе Старушки улыбались ей Мужчины кланялися ниже Ловили взор ее очей"
#
# arr=words.split()
#
#
# words_with_numbers = {value: len(value) for value in arr}
# print(words_with_numbers)

#
# dictionary = {
#     "Monday": 12,
#     "Tuesday": 14
# }
#
# new_with_Fahrenhait = {key: value * 9 / 5 + 32 for (key, value) in dictionary.items()}
#
# print(new_with_Fahrenhait)

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

dictionary = {row.letter: row.code for (index, row) in data.iterrows()}
print(dictionary)

while True:
    user_input = input("Enter a word ").upper()
    new_arr = [dictionary[value] for value in user_input]
    print(new_arr)
    break
