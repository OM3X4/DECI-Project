import random
import time

# Function for choosing options in the game
# Ensures that the player inputs a valid choice (either "1" or "0")
def choice(text):
    result = input(text)
    while result not in ["1", "0"]:
        print("Invalid choice")
        result = input(text)
    return result

# Function for random choices
# Returns a random choice between 1 and 0
def rand():
    return random.choice([1, 0])

# Function to print messages with a delay
# Prints the given message and waits for 1 second
def say(message):
    print(message)
    time.sleep(2)

# The main game function
def game():
    # Initialize score
    score = 0

    # Introduction to the story
    say("You stand at the edge of a dense forest, holding a map rumored to lead to the lost treasure of Eldoria.")
    
    # Prompt player to start the game or not
    start_choice = choice("Do you want to enter? (1 = yes, 0 = no): ")

    # End the game if the player chooses not to start
    if start_choice == "0":
        print("GAME OVER")
        return

    # Continue with the game if the player chooses to start
    say("With courage, you step into the forest.")
    say("You think you are strong enough to make it through the forest and take the treasure.")
    say("OK")

    # First choice: path selection
    path_choice = choice("You have two paths: left or right. Choose (left = 0, right = 1): ")

    # Determine outcome based on random choice
    if rand() == 1:
        say("You found a sword! (+10 points)")
        score += 10
    else:
        say("You found nothing.")
    say(f"Your current score is {score}")

    # If player chooses the left path
    if path_choice == "0":
        say("You find a stream with a shiny object in the water.")
        choice1 = choice("Examine it (1) or continue on your way (0): ")
        if choice1 == "1":
            if rand() == 1:
                say("Found a jeweled dagger (+20 points).")
                score += 20
            else:
                say("Encountered a snake and lost some health (-10 points).") 
                score -= 10
        say(f"Your current score is {score}")

    # If player chooses the right path
    if path_choice == "1":
        say("You find a weak bridge over a big hole.")
        say("Cross the bridge (1/2 chance of success) or look for another way around (1/2 chance of finding a hidden path).")

        choice2 = choice("Cross the bridge (1) or look for another way (0): ")

        if choice2 == "1":
            if rand() == 1:
                say("You cross safely and find an ancient stone tablet with strange markings (+20 points).")
                score += 20
            else:
                say("The bridge breaks and you fall, losing some health (-10 points).")
                score -= 10
        else:
            if rand() == 1:
                say("You find a hidden path that leads to a small treasure chest (+30 points).")
                score += 30
            else:
                say("You find nothing and waste time (no change).")
        say(f"Your current score is {score}")

    # Encounter at the entrance of a hidden cave
    say("You find the entrance of a hidden cave.")

    choice3 = choice("Enter the cave (1) or search the area around first (0): ")
    if choice3 == "0":
        if rand() == 1:
            say("You find a journal with a clue about a secret lever inside the cave (+20 points).")
            score += 20
        else:
            say("You waste time searching (no change).")
    say(f"Your current score is {score}")
    
    # Inside the cave
    say("Now you are inside the cave.")
    say("Inside, you hear dripping water and come to a fork in the path.")

    choice4 = choice("Take the left tunnel (1) or the right tunnel (0): ")

    if choice4 == "1":
        if rand() == 1:
            say("You encounter a dead end and lose time (no change).")
        else:
            say("You find a small treasure chamber (+30 points).")
            score += 30
    else:
        if rand() == 1:
            say("You find a hidden alcove with a treasure chest (+40 points).")
            score += 40
        else:
            say("You encounter a trap and lose some health (-10 points).")
            score -= 10
    say(f"Your current score is {score}")

    # Encounter with the mystical being guarding the treasure
    say("You find the secret lever and open a hidden door, revealing the treasure. It is guarded by a mystical being.")
    choice5 = choice("Negotiate with the guardian (1) or fight the guardian (0): ")

    if choice5 == "1":
        if rand() == 1:
            say("The guardian allows you to take some treasure (+50 points).")
            score += 50
        else:
            say("The guardian refuses and you lose time (no change).")
    else:
        if rand() == 1:
            say("You defeat the guardian and take the treasure (+100 points).")
            score += 100
        else:
            say("The guardian defeats you and you lose a lot of health (-40 points).")
            score -= 40
    say(f"Your current score is {score}")

    # End of the game
    say("************************Game Ended************************")
    say(f"Your final score is {score}")

    # Prompt player to start the game again
    start_again = choice("Do you want to start the game again? (yes = 1, no = 0): ")

    if start_again == "1":
        game()

# Start the game
game()
