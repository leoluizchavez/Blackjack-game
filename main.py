import random
import time

def total(cards):
    total = 0
    for i in range(len(cards)):
        total += cards[i]
    return total

def get_random_card():
    new_card = random.randint(1, 13)
    if new_card > 11:
        return 10
    elif new_card == 1:
        return 11
    else:
        return new_card

continue_game = True

while continue_game:
    player_card_1 = get_random_card()
    player_card_2 = get_random_card()
    player_cards = [player_card_1, player_card_2]
    player_rounds = 0

    player_total = total(player_cards) # player total score

    print(f"Card 1 : {player_card_1}")
    print(f"Card 2 : {player_card_2}")
    print(f"Total: {player_total}")

    while True:
        player_total = total(player_cards)

        if player_total == 21:
            print("You've got blackjack")
            break

        user_input = int(input("Enter 1 to add new card, 2 to stand: "))

        if user_input == 1:
            new_card = get_random_card()
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
        computer_card_1 = get_random_card()
        computer_card_2 = get_random_card()

        computer_cards = [computer_card_1,computer_card_2]
        computer_rounds = 0

        computer_total = total(computer_cards)
        time.sleep(1)
        print("Computer Turn")
        print(f"Computer card 1: {computer_card_1}")
        print(f"Computer card 2: {computer_card_2}")

        while computer_total < 21:
            computer_new_card = get_random_card()
            computer_cards.append(computer_new_card)
            computer_total = total(computer_cards)
            computer_rounds += 1
            time.sleep(.5)
            print(f"Computer have added {computer_rounds} card/s")
            time.sleep(.5)
            print(f"Computer got a {computer_new_card}")

        print(f"Computer Total: {computer_total}")

        if computer_total < 21 or (player_total < computer_total <= 21):
            print("Computer wins the game!")
        elif player_total == computer_total:
            print("It's a tie!")
        else:
            print("Player wins")

    continue_input = int(input("Enter 1 to play again or 2 to exit: "))

    if continue_input == 2:
        continue_game = False
        print("You've exit the game")


