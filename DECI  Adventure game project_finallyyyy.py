import time
import random

score = 40
places = ["school", "lab", "garden", "hospital", "strange home"]
persons = ["someone", "strange man", "crazy prof", "evil scientist"]
place = random.choice(places)
person = random.choice(persons)


def score_result():
    # Make score global
    global score

    if score == 100:
        # Slowing down the process to make it realistic
        time.sleep(2)
        # When you win the game
        print("Congratulations! You won the game.")
        time.sleep(2)
    elif score < 100:
        time.sleep(2)
        # When you lose the game
        print("You lost unfortunately.")
        time.sleep(2)

    print("The game is over")
    time.sleep(2)
    play_again()


def pl_ac_es():
    time.sleep(2)
    print(f"Imagine you find yourself in a {place}. While you walk a little,")
    time.sleep(2)
    print(f" you find {person} holding a strange syringe")
    time.sleep(2)
    print(" and quickly approaching you.")
    time.sleep(2)
    print("What would you do?")
    time.sleep(2)
    # The player chooses 1 if they want to escape
    print("Choose (1) if you would try to escape and call the police.")
    time.sleep(2)
    # The player chooses 2 if they want to attack him and call the police
    print("Choose (2) if you would try to")
    time.sleep(2)
    print("confront and deter them and call the police.")
    time.sleep(2)


def t_as_k():
    # Ask the player to choose an action
    choice = input("Choose 1 or 2: ")

    # When choice is not 1 or 2
    while choice not in ["1", "2"]:
        print("Invalid choice! Please enter 1 or 2.")
        choice = input("Choose 1 or 2: ")

    global score
    # Choosing to escape
    if choice == "1":
        time.sleep(2)
        print("You quickly run away and call the police.")
        time.sleep(2)
        print(f" They arrive just in time to catch the {person}!")
        time.sleep(2)
        print("You couldn’t escape, 30 points deducted.")
        time.sleep(2)
        # The points decrease
        score -= 30
        print(f"Your current score is: {score}")
        time.sleep(2)

    # Choosing to attack
    elif choice == "2":
        time.sleep(2)
        print(f"You bravely confront the {person}.")
        print(f" He backs away and leaves the {place}.")
        time.sleep(2)
        print("You managed to stop him, 30 points added.")
        time.sleep(2)
        # The points increase
        score += 30
        print(f"Your current score is: {score}")
        time.sleep(2)


def policeman():
    time.sleep(2)
    print(f"While the policeman was on his way,")
    time.sleep(2)
    print(f" the {person} ran away and tried to kill you.")
    time.sleep(2)
    print("What would you do?")
    time.sleep(2)
    print("Choose (1) to confront him again.")
    time.sleep(2)
    print("Choose (2) to escape and go to the police.")
    time.sleep(2)

    # Ask the player to choose an action
    choice = input("Choose 1 or 2: ")
    # When choice is not 1 or 2
    while choice not in ["1", "2"]:
        print("Invalid choice! Please enter 1 or 2.")
        choice = input("Choose 1 or 2: ")

    global score
    if choice == "1":
        time.sleep(2)
        print("You hit him with a chair and he passed out. Police arrived.")
        time.sleep(2)
        print("30 points added.")
        time.sleep(2)
        score += 30
        print(f"Your current score is: {score}")
    elif choice == "2":
        print("He trapped you, and you were killed. 30 points deducted.")
        time.sleep(2)
        score -= 30
        print(f"Your current score is: {score}")
        time.sleep(2)


def play_again():
    time.sleep(2)
    choice = input("Do you want to play again? (yes/no): ")
    # When choice is not yes or no
    while choice not in ["yes", "no"]:
        print("Invalid choice! Please enter yes or no.")
        choice = input("Do you want to play again? (yes/no): ")

    if choice == "yes":
        play_game()
    elif choice == "no":
        print("Thank you for playing")
        exit()


def play_game():
    print("Welcome to DECI Adventure game")
    time.sleep(2)
    print("The game began")
    time.sleep(2)
    pl_ac_es()
    t_as_k()
    policeman()
    score_result()


if __name__ == "__main__":
    play_game()
