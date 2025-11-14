import time

print("⚽ Welcome to the Football Match Simulator ⚽")
print("-----------------------------------------------")

# Function for safe number input
def write_number(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Enter a valid number")

# Function to decide the winner
def decide_winner(score1, score2, team1, team2):
    if score1 > score2:
        return f"{team1} wins 🎉🎉🎉."
    elif score2 > score1:
        return f"{team2} wins 🎉🎉🎉."
    else:
        return "Draw"

# Function to handle extra time
def extra_time(score1, score2, team1, team2):
    print("Draw, heading into Extra Time 😱")
    et1 = write_number(f"Extra time goals by {team1}: ")
    et2 = write_number(f"Extra time goals by {team2}: ")
    score1 += et1
    score2 += et2
    winner = decide_winner(et1, et2, team1, team2)
    return score1, score2, winner, (et1, et2)

# Function to handle penalty shootout
def penalties(team1, team2):
    print("Scores still level. Time for penalties! 😮")
    p1 = write_number(f"Penalties scored by {team1}: ")
    p2 = write_number(f"Penalties scored by {team2}: ")
    if p1 > p2:
        return f"{team1} wins the Penalty Shootout 🎉🎉🎉"
    elif p2 > p1:
        return f"{team2} wins the Penalty Shootout 🎉🎉🎉"
    else:
        return "We cannot decide a winner"

# List to store match history
matches = []

# Main game loop
while True:
    # Ask for team names
    team1 = input("Enter the first team's name: ").title()
    team2 = input("Enter the second team's name: ").title()

    # Ask for scores
    score1 = write_number(f"Enter {team1} score: ")
    score2 = write_number(f"Enter {team2} score: ")

    # Decide normal time winner
    result = decide_winner(score1, score2, team1, team2)

    # If draw, handle extra time and penalties
    if result == "Draw":
        score1, score2, et_result, extra_scores = extra_time(score1, score2, team1, team2)
        if et_result == "Draw":
            result = penalties(team1, team2)
        else:
            result = et_result

    print(result)

    # Store match history
    matches.append({
        "Team1": team1,
        "Team2": team2,
        "Score": f"{score1}-{score2}",
        "Result": result
    })

    # Play again?
    play_again = input("Do you want to play another match? (yes/no): ").lower()
    if play_again != "yes":
        print("\nThanks for playing! ⚽ Goodbye!\n")
        print("Match History:")
        for match in matches:
            print(f"{match['Team1']} vs {match['Team2']} - {match['Score']} | {match['Result']}")
        break


