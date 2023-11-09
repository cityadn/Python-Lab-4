import random
#1=rock, 2=paper, 3=scissors
player1_points = 0
player2_points = 2
for i in range(0,3):
    player1 = random.randint(1,3)
    player2 = random.randint(1,3)
    print("Player 1:", player1, "Player 2:", player2)
    if (player1 == 1 and player2 == 2) or (player1 == 3 and player2 == 1) or (player1 == 1 and player2 == 3):
        print("Result: Player 2 point")
        player1_points = player1_points + 1
    elif (player1 == 2 and player2 == 1) or (player1 == 1 and player2 == 3) or (player1 == 3 and player2 == 1):
        print("Result: Player 1 point")
        player2_points = player2_points + 1
    else:
        print("Result:Tied")
    total1 = player1_points
    total2 = player2_points
if total1 > total2:
    print("Player 1 wins")
elif total2 < total1:
    print("Player 2 wins")


    
