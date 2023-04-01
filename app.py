from utils import Database
"""
user menu that control to add a new cast, list cast numbers or delete cast numbers
"""

OPTION = """ Enter the option you want to do:
— 'a': add new type cast you use
— 'l': list all casts you use
— 'd': remove the cast
— 'q': quit:\n

"""
BENEFIT = """ Enter the benefit package:

— 'n': Nation Health Insurance
— 'o': own expense:\n

"""

CAST = """ Enter the cast you used:
— 'head': three-point head cast
— 'T': four-point head and neck cast
— 'ABD': Abdomen cast
— 'ABD-cut': Abdomen-cut cast
— 'pelvis': pelvis cast:\n

"""


def menu():
    user_option = input(OPTION)
    while user_option != 'q':
        if user_option == 'a':
            prompt_add_cast()
        elif user_option == 'l':
            prompt_list_cast()
        user_option = input(OPTION)


def prompt_add_cast():

    benefit = input(BENEFIT)
    for character in benefit:
        if character == 'n':
            benefit = 'NHI'
        elif character == 'o':
            benefit = 'own expense'
        else:
            break

    cast = input(CAST)
    Database.add_cast(benefit, cast, 1)


def prompt_list_cast():
    casts = Database.get_all_casts()
    for cast in casts:
        print(f'Date: {cast["Date"]}\nBenefit—{cast["Benefit package"]}, '
              f'{cast["cast"]}:{cast["number"]}' )


menu()
