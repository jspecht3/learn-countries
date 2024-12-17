from utils import str_eq, inc_str, other_str


def skeleton(gamemode, selection):
    challenge = selection.copy()
    next_challenge = challenge.copy()

    scores = []
    totals = []

    while len(challenge) > 0:
        score = 0
        increment = 0

        totals.append(len(challenge))
        total = totals[-1]

        print(f"\n --- Beginning Round {len(totals)} ---")

        for current in challenge:
            increment += 1

            guess = input(f"\nWhat is the {gamemode} of {
                          current.__dict__["name"][0]}?\n  Guess: ")
            correct = str_eq(guess, current.__dict__[gamemode])

            if correct:
                score += 1
                others = other_str(guess, current.__dict__[gamemode])
                next_challenge.remove(current)

                print(f"Correct! Current Score: {
                      score}/{increment} ({total})")
                if 0 != len(others):
                    print(f"  Other {gamemode}s include: {others}")
                continue

            while (not correct):
                to_type = inc_str(current.__dict__[gamemode])
                guess = input(f"Incorrect, type {
                              to_type} to continue.\n  Guess: ")
                correct = str_eq(guess, current.__dict__[gamemode])

            print(f"Current Score: {score}/{increment} ({total})")
        scores.append(score)

        print(f"\n*** Round {len(totals)} Score: {score}/{total} ***\n")
        challenge = next_challenge.copy()

    print(f"\n----- Quiz Completed in {len(totals)} Rounds -----\n")
    for i in range(len(totals)):
        score_out = round(scores[i] / totals[i], 4) * 100
        print(f"  Round {i+1} Score: {scores[i]}/{totals[i]}, {score_out}%")
