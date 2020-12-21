from collections import defaultdict

all_ingredients = []
candidates = defaultdict(list)

with open('in', 'r') as f:
    for line in f.readlines():
        ingredients, allergens = line.split(' (')
        ingredients = ingredients.strip().split()
        allergens = allergens.replace('contains ', '').replace(')', '').strip().split(', ')

        all_ingredients += ingredients

        for allergen in allergens:
            candidates[allergen].append(set(ingredients))

are_allergens = set()
for allergen in candidates.keys():
    options = set(all_ingredients)
    for i in candidates[allergen]:
        options = options.intersection(i)

    for i in options:
        are_allergens.add(i)

count = 0
for ingredient in all_ingredients:
    if ingredient not in are_allergens:
        count += 1

print(count)
