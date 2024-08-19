import random

print("=====================")
print("Random Food Generator")
print("=====================")

def random_food_generator(meal_count):
    foods = [
        "Pizza",
        "Burger",
        "Sushi",
        "Pasta",
        "Salad",
        "Tacos",
        "Ice Cream",
        "Fried Rice",
        "Sandwich",
        "Steak",
        "Vegetable Stir Fry",
        "Pancakes",
        "Ramen",
        "Curry",
        "Donuts",
        "Burritos",
        "Spaghetti",
        "Omelette",
        "Chicken Wings",
        "Quiche",
        "BBQ Ribs",
        "Lasagna",
        "Gyro",
        "Fish and Chips",
        "Falafel",
        "Chicken Alfredo",
        "Baked Ziti",
        "Gumbo",
        "Chili",
        "Lobster Roll",
        "Clam Chowder",
        "Beef Stew",
        "Mac and Cheese",
        "Fajitas",
        "Hot Dogs",
        "Grilled Cheese",
        "Shrimp Scampi",
        "Chicken Parmesan",
        "Pad Thai",
        "Stuffed Peppers",
        "Shepherd's Pie",
        "Moussaka",
        "Empanadas",
        "Enchiladas",
        "Stuffed Cabbage Rolls",
        "Risotto",
        "Meatloaf",
        "Pot Roast",
        "Bangers and Mash",
        "Pulled Pork Sandwich",
        "Shakshuka",
        "Pho",
        "Paella",
        "Dim Sum",
        "Miso Soup",
        "Gnocchi",
        "Beef Tacos",
        "Chicken Quesadilla",
        "Lentil Soup",
        "Gazpacho",
        "Kebab",
        "Bruschetta",
        "Spanakopita",
        "Ceviche",
        "Beef Wellington",
        "Chicken Pot Pie",
        "Croque Monsieur",
        "Crab Cakes",
        "French Onion Soup",
        "Tofu Stir Fry",
        "Eggplant Parmesan",
        "Chicken and Waffles",
        "Peking Duck",
        "Tamales",
        "Jambalaya",
        "Baba Ganoush",
        "Samosas",
        "Pierogi",
        "Ratatouille",
        "Chicken Tikka Masala",
        "Gyoza",
        "Kimchi",
        "Churros",
        "Chocolate Cake",
        "Apple Pie",
        "Crepes",
        "Baklava",
        "Bread Pudding",
        "Mango Sticky Rice",
        "Tiramisu",
        "Eclair",
        "Pavlova",
        "Banoffee Pie",
        "Cheesecake",
        "Key Lime Pie"
    ]
    
    return random.sample(foods, min(meal_count, len(foods)))

if __name__ == "__main__":
    meal_count = 0
    while meal_count < 1 or meal_count > 5:
        meal_count = input("How many meals do you want to generate (1-5)? ")
        if not meal_count.isdigit():
            print("Please enter a valid number between 1 and 5.")
            meal_count = 0
        else:
            meal_count = int(meal_count)
            if meal_count < 1 or meal_count > 5:
                print("Please enter a number between 1 and 5.")

    meals = random_food_generator(meal_count)
    print("***************************")
    print("Meal or snack suggestions: ")
    print("***************************")
    for meal in meals:
        print("- " + meal)
