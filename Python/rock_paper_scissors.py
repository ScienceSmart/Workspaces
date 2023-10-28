#A two-player Rock-Paper-Scissors game

answer = ""
user1 = input("What is your name, Player 1: ")
user2 = input("And what is your name, Player 2: ")

while (answer != "no"):
    player1 = input("Enter rock, paper or scissors: ")
    player2 = input("Enter rock, paper, or scissors: ")
    if (player1 == player2):
        print("It is a draw. You can go again. ")
    elif player1 == "rock":
        if player2 == "scissor":
            print(f"Congratulations {user1}. ")
        else: 
            print(f"Congratulations {user2}. ")
    elif player1 == "scissor":
        if player2 == "paper":
            print(f"Congratulations {user1}. ")
        else: 
            print(f"Congratulations {user2}. ")
    elif player1 == "paper":
        if player2 == "rock":
            print(f"Congratulations {user1}. ")
        else: 
            print(f"Congratulations {user2}. ")
    else:
        print("You have to write a valid input. Try again!")
    answer = input("Enter yes to start a new game or no to end it: ")

