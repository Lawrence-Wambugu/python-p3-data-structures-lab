# data_structures.py

def get_names(food_list):
    """
    Function to retrieve names from a list of food dictionaries.
    """
    return [food['name'] for food in food_list]

def get_spiciest_foods(food_list):
    """
    Function to return foods with a heat_level greater than 5.
    """
    return [food for food in food_list if food['heat_level'] > 5]

def print_spicy_foods(food_list):
    """
    Function to print all foods formatted with 🌶 emojis according to their heat level.
    """
    for food in food_list:
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")

def get_spicy_food_by_cuisine(food_list, cuisine):
    """
    Function to return the food that matches a given cuisine.
    """
    for food in food_list:
        if food['cuisine'] == cuisine:
            return food
    return None  # Return None if no match is found

def print_spiciest_foods(food_list):
    """
    Function to print foods with a heat_level greater than 5 formatted with 🌶 emojis.
    """
    for food in get_spiciest_foods(food_list):
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")

def get_average_heat_level(food_list):
    """
    Function to return the average of heat levels in the list of spicy foods.
    """
    total_heat = sum(food['heat_level'] for food in food_list)
    return total_heat / len(food_list) if food_list else 0

def create_spicy_food(food_list, new_food):
    """
    Function to add a new spicy food to the list and return the updated list.
    """
    food_list.append(new_food)
    return food_list
