import random


# Coin list
heads_Counter = 0
tails_Counter = 0
test_run_times = 100
test = 0
coin =("Heads", "Tails")
while test <=99:
    test += 1
    if random.choice(coin) == "Heads":
        heads_Counter +=1
    else:
        tails_Counter +=1



print(f"The outcome from the Coin flipped 100 times is Heads: {heads_Counter} Times. and Tails: {tails_Counter} Times.")

