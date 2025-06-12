sport = "Hockey"
p1_score = 1
p2_score = 1

if p1_score == p2_score:
    print("It's a draw!")
elif sport.lower() == "golf":
    if p1_score < p2_score:
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")
elif sport.lower() == "basketball":
    if p1_score > p2_score:
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")
else:
    print("Unknown sport!")

