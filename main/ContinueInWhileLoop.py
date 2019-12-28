import random

playerHp = 260
enemyAtkL = 60
enemyAtkH = 80

while playerHp > 0:
    dmg = random.randrange(enemyAtkL, enemyAtkH)
    playerHp = playerHp - dmg

    if playerHp <= 30:
        playerHp = 30

    print("Enemy strick for", dmg, "point of damage.")
    print("Current Hp are: ", playerHp)
    print("-----")

    if playerHp > 30:
        continue

    print("You're Hp are low ...")
    print("You have been teleport too a safer place")
    break
