# Random Name Generator
import random
import csv

shut_down = False

# Web scraped baby names of various origins from adoption.com and saved as separate csv files
origins = ['Armenian', 'Cambodian', 'Egyptian', 'Indian', 'Irish', 'Japanese', 'Korean', 'Native-american', 'Polish',
           'Thai']
while not shut_down:
    # Every name is categorized as either a male/female dominated name. User can select a male/female/either name.
    gender = (input("Let me recommend you a name. Should I recommend a male, female, or any name? \n")).lower()

    while gender != 'male' and gender != 'female' and gender != 'any':
        print("That is not an option. Please enter 'male', 'female', or 'any'.")
        gender = (input("Should I recommend a male, female, or any name? \n")).lower()

    # Have user select an origin to fetch the csv file of origin of choice
    origin = (input(f"I can recommend a name from various origins.\n Please choose one of the following: {origins} "
                    f"\n")).capitalize()

    while origin not in origins:
        print("Sorry,that is not an available option.")
        origin = (input(f"Please choose one of the following: {origins} \n")).capitalize()

    if origin == 'Japanese':
        input_file = csv.DictReader(open('japan_names.csv'))
    elif origin == 'Thai':
        input_file = csv.DictReader(open('thai_names.csv'))
    elif origin == 'Indian':
        input_file = csv.DictReader(open('indian_names.csv'))
    elif origin == 'Cambodian':
        input_file = csv.DictReader(open('cambodian_names.csv'))
    elif origin == 'Egyptian':
        input_file = csv.DictReader(open('egyptian_names.csv'))
    elif origin == 'Armenian':
        input_file = csv.DictReader(open('armenian_names.csv'))
    elif origin == 'Korean':
        input_file = csv.DictReader(open('korean_names.csv'))
    elif origin == 'Native-american':
        input_file = csv.DictReader(open('native_american_names.csv'))
    elif origin == 'Polish':
        input_file = csv.DictReader(open('polish_names.csv'))
    elif origin == 'Irish':
        input_file = csv.DictReader(open('irish_names.csv'))

    # Transfer data in selected csv file as a list of dictionaries
    dict_list = []
    for rows in input_file:
        dict_list.append(rows)

    # Used Random module to select a random name in list
    file_size = len(dict_list)
    random_index = random.randrange(0, file_size)

    if gender != 'any':
        # Generate a new random index and subsequent name if it does not match requested gender type
        while (dict_list[random_index]["Gender"]).lower() != gender:
            random_index = random.randrange(0, file_size)

    name = dict_list[random_index]["Name"]
    meaning = dict_list[random_index]["Meaning"]

    print(f"I recommend the name {name}. It means '{meaning}' in that country! :)\n")

    # Restart the generator until the user decides to shut it off
    keep_going = input("Do you want me to recommend another name? Type 'yes' or 'no': \n")
    if keep_going == 'no':
        shut_down = True
        print("Goodbye! I hope you liked my recommendation.")
