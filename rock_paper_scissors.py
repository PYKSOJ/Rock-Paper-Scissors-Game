import random
from play import play
while True:
    player = input("[r]ock, [p]aper, [s]cissors \nwhat U chose :")
    if player != "r" and player != "p" and player != "s" :
        break
    else:
        play(player)
