
print("⚽ Welcome to the Football Match Simulator ⚽")
print("-----------------------------------------------")

#Ask for team names
while True:
    team1 = input("Enter the first teams name: ").upper()
    team2 = input("Enter the second teams name: ").upper()

#Ask for scores of each team
    score1= int(input(f"Enter {team1} score: "))
    score2= int(input(f"Enter {team2} score: "))

# This play out all the possibilities available such as win,lose and draw
    if score1 > score2:
        print(f"{team1} wins 🎉🎉🎉.")
    elif score1 < score2:
        print(f"{team2} wins 🎉🎉🎉.")
    elif score1 == score2:
        print("Draw, We head into Extra Time 😱")

# since it is a draw we have to go to extra time and these are the scores
        et1 = int(input(f"Extra time goals by {team1}: "))
        et2 = int(input(f"Extra time goals by {team2}: "))

        score1 += et1
        score2 += et2

# This part will show the outcome during extra time
        if et1 > et2:
           print(f"{team1} wins 🎉🎉🎉.")
        elif et1 < et2:
           print(f"{team2} wins 🎉🎉🎉.")
        elif et1 == et2:
           print("The scores are still level as we end Extra time, We will need Penalties 😮")

           #Since it was a draw, this part will allow the penalty shootout to happen
           p1 = int(input(f"Number of penalties scored by {team1}: "))
           p2 = int(input(f"Number of penalties scored by {team2}: "))

           score1 += p1
           score2 += p2

#This will show the outcomes that occured during the penalty shootout
        if p1 > p2:
              print(f"{team1} wins the Penalty Shootout 🎉🎉🎉")
        elif p1 < p2:
               print(f"{team2} wins the Penalty Shootout 🎉🎉🎉")
        else:
               print("We cannot decide a winner ")

#This part will for another match or if not the game ends
    play_again = input("Do you want to play another match? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing! ⚽ Goodbye!")
        break


else:
    print("Invalid input")