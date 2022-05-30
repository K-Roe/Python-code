import random
from tabulate import tabulate
import matplotlib.pyplot as plt

# Coin list
heads_Counter = 0
tails_Counter = 0
test_run_times = 100
test = 1
coin =("Heads", "Tails")
while test <= test_run_times:
    test += 1
    if random.choice(coin) == "Heads":
        heads_Counter +=1
    else:
        tails_Counter +=1


#create data

data = [["Heads", heads_Counter],
        ["Tails", tails_Counter]]
#header names
col_names = ["Coin", "Times flipped"]
#disply table
print(tabulate(data, headers=col_names))

#Create pie chart to show outcome
labels = ["Heads", "Tails"]
Flipped = [heads_Counter, tails_Counter]
plt.pie(Flipped, labels=labels,
        autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')
plt.show()