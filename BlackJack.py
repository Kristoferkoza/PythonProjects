import random

list_of_cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
dict_of_values = {'J': 2, 'Q': 3, 'K': 4, 'A': 11}

print(random.choice(list_of_cards))

def add_card():
    choice = random.choice(list_of_cards)
    return choice

def count(deck):
    result = 0
    for i in deck:
        if i == 'J' or i == 'Q' or i == 'K' or i == 'A':
            result += dict_of_values[i]
        else:
            result += i

    return result
    
def print_deck(deck):
    for i in deck:
        print(i)

def info_for_player(player_deck, computer_deck):
    print(f"Player Cards: {player_deck}. Value: {count(player_deck)}.")
    print(f"Computer Cards: {computer_deck}. Value: {count(computer_deck)}.")

def gameStart():
    print("WELCOME IN BLACKJACK GAME!")

#----------------MAIN----------------
your_score = 0
computer_score = 0
draws = 0
play_again = 'y'

while play_again == 'y':
    player_deck = []
    player_value = 0
    computer_deck = []
    computer_value = 0

    player_deck.append(add_card())
    player_deck.append(add_card())
    computer_deck.append(add_card())

    info_for_player(player_deck, computer_deck)
    player_value = count(player_deck)
    computer_value = count(computer_deck)

    take_card = input("Do you want to take a card? Yes - y, No - n: ")
    while(take_card == 'y' and player_value < 21):
        card = add_card()
        print(f"Your taken card is {card}.")
        player_deck.append(card)
        info_for_player(player_deck, computer_deck)
        player_value = count(player_deck)
        print()

        if player_value >= 21:
            break

        take_card = input("Do you want to take a card? Yes - y, No - n: ")

    if player_value == 21:
        print("Value of your cards equals 21, you won!")
        your_score += 1
    elif player_value > 21:
        print("Value of your cards equals more than 21, you lost.")
        computer_score += 1
    else:
        print()
        print("Now it is computer turn!")
        while computer_value < player_value and computer_value < 17:
            card = add_card()
            print(f"Taken card by computer is {card}.")
            computer_deck.append(card)
            print(f"Computer Cards: {computer_deck}. Value: {count(computer_deck)}.")
            computer_value = count(computer_deck)
        
        print()
        if computer_value == 21:
            print("Value of computer's cards equals 21, you lost!")
            computer_score += 1
        elif computer_value > 21:
            print("Value of computer's cards equals more than 21, you won.")
            your_score += 1
        else:
            if player_value == computer_value:
                print("Value of your cards is equal value of computer's cards, it is a draw.")
                draws += 1
            elif player_value > computer_value:
                print("Value of your cards is higher than value of computer's cards, you won.")
                your_score += 1
            else:
                print("Value of your cards is lower than value of computer's cards, you lost.")
                computer_score += 1

    play_again = input("Do you want to play again? Yes - y, No - n: ")

num_of_games = your_score + computer_score + draws
winning_percentage = round(your_score/num_of_games * 100, 0)
    
print("Thank you for playing my game! Here are your results: ")
print(f"You played {num_of_games} games.")
print(f"You won {your_score} games!")
print(f"Computer won {computer_score} games.")
print(f"{draws} games ended with a draw.")

print(f"You won {winning_percentage}% of games! Congratulations!")


