import random

def total(cards):
    total = 0
    for i in range(len(cards)):
        total += cards[i]
    return total

player_card_1 = random.randint(1, 11)
player_card_2 = random.randint(1, 11)
player_cards = [player_card_1, player_card_2]
player_rounds = 0

player_total = total(player_cards) # player total score

print(f"Card 1 : {player_card_1}")
print(f"Card 2 : {player_card_2}")
print(f"Total: {player_total}")

while True:
    user_input = int(input("Enter 1 to add new card, 2 to stand: "))

    if user_input == 1:
        new_card = random.randint(1,11)
        player_cards.append(new_card)
        player_total = total(player_cards)
        player_rounds += 1
        print(f"You've added {player_rounds} card/s")
        print(f"New Card: {new_card}")
        print(f"Total: {player_total}")

        if player_total > 21:
            print("You lose")
            break

        elif player_total == 21:
            print("You've got blackjack! You win!")
            break

    elif user_input == 2:
        print("You choose to stand")
        break

    else:
        print("Please choose a valid number! ")


if user_input == 2:
    computer_card_1 = random.randint(1, 11)
    computer_card_2 = random.randint(1, 11)

    computer_cards = [computer_card_1,computer_card_2]
    computer_rounds = 0

    computer_total = total(computer_cards)
    print("Computer Turn")
    print(f"Computer card 1: {computer_card_1}")
    print(f"Computer card 2: {computer_card_2}")

    while computer_total < 21:
        computer_new_card = random.randint(1, 11)
        computer_cards.append(computer_new_card)
        computer_total = total(computer_cards)
        computer_rounds += 1
        print(f"Computer have added {computer_rounds} card/s")
        print(f"Computer got a {computer_new_card}")

    print(f"Computer Total: {computer_total}")

    if computer_total < 21 or (player_total < computer_total <= 21):
        print("Computer wins the game!")
    elif player_total == computer_total:
        print("It's a tie!")
    else:
        print("Player wins")



# print(f" Card 1: {card_1}")
# print(f" Card 2: {card_2}")
# print(f" Sum : {sum}")

# user_input = int(input(" Enter 1 to pick a new card and 2 to stand: "))
#
# while sum < 21:
#     if user_input == 1:
#         sum = card_1 + card_2



