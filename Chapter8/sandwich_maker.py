import pyinputplus as pyip
import pprint

def sandwich_maker():
    sandwich = {'bread': '', 'protein': '', 'cheese': '', 'condiments': '', 'quantity': 0}
    price = 0
    bread = pyip.inputMenu(['wheat', 'white', 'sourdough'], numbered=True)
    sandwich['bread'] = bread
    if bread == 'wheat': price += 1
    elif bread == 'white': price += 1.5
    elif bread == 'sourdough': price += 2
    protein = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'], numbered=True)
    sandwich['protein'] = protein
    if protein == 'chicken': price += 3
    elif protein == 'turkey': price += 3.5
    elif protein == 'ham': price += 4
    elif protein == 'tofu': price += 2
    cheese = pyip.inputYesNo('Would you like cheese? ')
    if cheese == 'yes':
        cheese_type = pyip.inputMenu(['cheddar', 'Swiss', 'mozzarella'], numbered=True)
        sandwich['cheese'] = cheese_type
    if cheese_type == 'cheddar': price += 1
    elif cheese_type == 'Swiss': price += 1.5
    elif cheese_type == 'mozzarella': price += 2
    condiments = pyip.inputYesNo('Would you like condiments? ')
    if condiments == 'yes':
        condiment = pyip.inputMenu(['mayo', 'mustard', 'lettuce', 'tomato'], numbered=True)
        sandwich['condiments'] = condiment
    how_many_sandwiches = pyip.inputInt('How many sandwiches would you like? ', min=1)
    sandwich['quantity'] = how_many_sandwiches

    pprint.pprint(f'You ordered {sandwich["quantity"]} {sandwich["bread"]} {sandwich["protein"]} sandwich(es) with {sandwich["cheese"]} cheese and {sandwich["condiments"]}.Your total is ${price * sandwich["quantity"]}')

sandwich_maker()