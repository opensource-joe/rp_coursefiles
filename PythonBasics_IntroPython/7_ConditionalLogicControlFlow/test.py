# Example: Evaluate the Winner
# - Two people play either basketball or golf.
# - They tell you what sport they have been playing and their score.
# - You have to evaluate who won.
# - In golf, the lower score wins. In basketball, the higher score wins.

sport = "golf"
p1_score = 1
p2_score = 9

if p1_score == p2_score:
    print("It's a draw!")

elif sport == "golf":
    if p1_score < p2_score:
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")

elif sport == "basketball":
    if p1_score > p2_score:
        ("Player 1 wins!")
    else:
        print("Player 2 wins!")

else:
    print("Unknown sport!")