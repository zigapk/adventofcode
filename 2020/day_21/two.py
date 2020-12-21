from collections import defaultdict

all_ingredients = []
candidates = defaultdict(list)
all_allergens = set()

with open('in', 'r') as f:
    for line in f.readlines():
        ingredients, allergens = line.split(' (')
        ingredients = ingredients.strip().split()
        allergens = allergens.replace('contains ', '').replace(')', '').strip().split(', ')

        all_ingredients += ingredients

        for allergen in allergens:
            all_allergens.add(allergen)
            candidates[allergen].append(set(ingredients))

allergen_to_candidate = {}
for allergen in candidates.keys():
    options = set(all_ingredients)
    for i in candidates[allergen]:
        options = options.intersection(i)

    allergen_to_candidate[allergen] = options

while sum([len(allergen_to_candidate[i]) for i in allergen_to_candidate.keys()]) != len(all_allergens):
    for allergen in all_allergens:
        if len(allergen_to_candidate[allergen]) == 1:
            # remove this allergen from all the other options
            candidate = list(allergen_to_candidate[allergen])[0]
            for allergen2 in all_allergens:
                if allergen2 == allergen:
                    continue
                if candidate in allergen_to_candidate[allergen2]:
                    allergen_to_candidate[allergen2].remove(candidate)

result = []
for k in allergen_to_candidate.keys():
    result.append((k, list(allergen_to_candidate[k])[0]))

result.sort()

print(','.join([i[1] for i in result]))
