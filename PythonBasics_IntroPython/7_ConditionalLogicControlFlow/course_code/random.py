import random

def coin_flip():
    if random.randint(0, 1) == 0:
        return "heads"
    else:
        return "tails"


def unfair_coin_flip(probability_of_tails):
    if random.random() < probability_of_tails:
        return "tails"
    else:
        return "heads"
    

heads_tally = 0
tails_tally = 0

for trial in range(100_000):
    if unfair_coin_flip(0.4) == "heads":
        heads_tally = heads_tally + 1
    else:
        tails_tally = tails_tally + 1

print("heads", heads_tally)
print("tails", tails_tally)
