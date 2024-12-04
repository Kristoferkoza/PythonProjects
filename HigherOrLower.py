import random
poland_players_dict = {
"Zielinski":35,
"Lewandowski":30,
"Kiwior":25,
"Cash":25,
"Zalewski":20,
"Szymanski":18,
"Bednarek":14,
"Kaminski":12,
"Moder":10,
"Szczesny":10
}

def correct_answer(player1, player2):
    result = ''
    if poland_players_dict[player1] > poland_players_dict[player2]:
        result = '>'
    elif poland_players_dict[player1] == poland_players_dict[player2]:
        result = '='
    else:
        result = '<'

    return result

def show_info(player1, player2):
    print(f"{player1}'s value is {poland_players_dict[player1]}M€")
    print(f"{player2}'s value is {poland_players_dict[player2]}M€")

poland_players_list = list(poland_players_dict.keys())
all_players_num = len(poland_players_list)

#------------------START--------------------
score = 0
play = True
player1 = None
player2 = random.choice(poland_players_list)



while play:
    player1 = player2
    player2 = random.choice(poland_players_list)
    while player1 == player2:
        player2 = random.choice(poland_players_list)
    
    print(f"Player 1 is {player1} and player 2 is {player2}.")
    player_answer = input("Which player is more expensive (or their value is equal)? Choose <, > or = : ")
    answer = correct_answer(player1, player2)

    print()
    if player_answer == answer:
        print("Your answer is correct!")
        show_info(player1, player2)
        score += 1
    else:
        print("Your answer is wrong!")
        show_info(player1, player2)
        play = False

print()
print(f"Your final score is {score}.")

