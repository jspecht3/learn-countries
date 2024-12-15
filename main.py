from lists import countries, asia, eu, af, na, sa, au, me, balkan
from data import germany, switzerland, lithuania


def str_eq(str1, list1):
    list2 = []
    for item in list1:
        list2.append(item.lower())
    return str1.lower() in list2


def other(str1, list1):
    list2 = []
    for item in list1:
        list2.append(item.lower())

    loc = list2.index(str1)
    del list1[loc]

    return list1


def other_str(str1, list1):
    others = other(str1, list1)
    if len(others) == 0:
        return ''

    to_return = ''
    for item in others:
        to_return += f"{item}, "
    return to_return[0:-2]


def inc_str(list1):
    to_return = ''
    if len(list1) != 1:
        to_return += ("one of ")

    for item in list1:
        to_return += (f"{item}, ")

    return to_return[0:-2]


def start(region):
    challenge = region.copy()
    next_countries = challenge.copy()

    scores = []
    totals = []

    while len(challenge) > 0:
        score = 0
        increment = 0

        totals.append(len(challenge))
        total = totals[-1]

        print(f"\n ----- Beginning Round {len(totals)} -----")

        for country in challenge:
            increment += 1

            guess = input(f"\nWhat is the capital of {
                          country.name[0]}?\n  Guess: ")
            correct = str_eq(guess, country.capital)

            if correct:
                score += 1
                others = other_str(guess, country.capital)
                next_countries.remove(country)

                print(f"  Correct! Current Score: {
                    score}/{increment} ({total})")
                if 0 != len(others):
                    print(f"  Other capitals include: {others}")
                continue

            while (not correct):
                to_type = inc_str(country.capital)
                guess = input(f"Incorrect, type {
                    to_type} to continue.\n  Guess: ")
                correct = str_eq(guess, country.capital)

            print(f"  Current Score: {score}/{increment} ({total})")
        scores.append(score)

        print(f"\n *** Round {len(totals)} Score: {score}/{total} *** \n")
        challenge = next_countries.copy()

    print(f"\n ----- Quiz Completed in {len(totals)} Rounds -----\n")
    for i in range(len(totals)):
        score_out = round(scores[i] / totals[i], 4) * 100
        print(
            f"  Round {i + 1} Score: {scores[i]}/{totals[i]}, {score_out}%")


region = input("Welcome! begin by selecting a region from the following:\n  countries, asia, europe (eu), africa (af), north america (na), south america (sa), oceania (au), middle east (me), or balkan. \n Region Selected: ")

regions = [countries, asia, eu, af, na, sa, au, me, balkan]


def variable_name(var):
    for name, value in globals().items():
        if value is var:
            return name


names = []
for name in regions:
    names.append(variable_name(name))

in_names = region in names

while not in_names:
    region = input(" Enter a valid region: ")
    in_names = region in names

print(f'--- Beginning {region} Capital Quiz ---')

index = names.index(region)
# start(regions[index])
start([germany, lithuania, switzerland])
