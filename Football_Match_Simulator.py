while True:
    # Get team names
    team1 = input("Enter Team 1 name: ").title().strip()
    team2 = input("Enter Team 2 name: ").title().strip()

    # Get scores for normal time
    score1 = int(input(f"Goals by {team1}: "))
    score2 = int(input(f"Goals by {team2}: "))

    # --- Normal Time Results ---
    if score1 > score2:
        print(f"{team1} wins 🎉🎉🎉.")
    elif score1 < score2:
        print(f"{team2} wins 🎉🎉🎉.")
    else:
        print("Draw! We head into Extra Time 😱")

        # --- Extra Time ---
        et1 = int(input(f"Extra time goals by {team1}: "))
        et2 = int(input(f"Extra time goals by {team2}: "))

        score1 += et1
        score2 += et2

        if score1 > score2:
            print(f"{team1} wins in Extra Time 🎉🎉🎉.")
        elif score1 < score2:
            print(f"{team2} wins in Extra Time 🎉🎉🎉.")
        else:
            print("Still level after Extra Time 😮 We go to Penalties!")

            # --- Penalty Shootout ---
            p1 = int(input(f"Penalties scored by {team1}: "))
            p2 = int(input(f"Penalties scored by {team2}: "))

            if p1 > p2:
                print(f"{team1} wins the Penalty Shootout 🎉🎉🎉.")
            elif p1 < p2:
                print(f"{team2} wins the Penalty Shootout 🎉🎉🎉.")
            else:
                print("We cannot decide a winner! 😵")

    # --- Play Again or Quit ---
    play_again = input("Do you want to play another match? (yes/no): ").lower().strip()
    if play_again != "yes":
        print("Thanks for playing! ⚽ Goodbye!")
        break



else:

    print("Invalid input")

