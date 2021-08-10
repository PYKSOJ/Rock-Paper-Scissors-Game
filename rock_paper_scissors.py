import random

def play(player):
    # m = ["r", "p", "s"]
    d = {"r": "rock", "p": "paper", "s": "scissors"}
    # computer = m[random.randrange(len(m))]
    computer = random.choice(list(d.keys()))
    if player == computer:
        result = "tie"
    elif player == "r":
        if computer == "s":
            result = "player win"
        else:
            result = "computer win"
    elif player  == "p":
        if computer == "r":
            result = "player win"
        else:
            result = "computer win"
    elif player == "s":
        if computer == "p":
            result = "player win"
        else:
            result = "computer win"
    # print("Player choose ", d[player], "and computer choose", d[computer], "and result is ", result)
    print("player choose {} and computer choose {} and result is {}". format(d[player], d[computer], result))

while True:
    player = input("[r]ock, [p]aper, [s]cissors \nwhat U chose :")
    if player != "r" and player != "p" and player != "s" :
        break
    else:
        play(player)