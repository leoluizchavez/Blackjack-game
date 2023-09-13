import random

def total(cards):
    total = 0
    for i in range(len(cards)):
        total += cards[i]
    return total

card_1 = random.randint(1,11)
card_2 = random.randint(1,11)
cards = [card_1,card_2]
rounds = 0

current_total = total(cards)

print(f"Card 1 : {card_1}")
print(f"Card 2 : {card_2}")
print(f"Total: {current_total}")

while True:
    user_input = int(input("Enter 1 to add new card, 2 to stand: "))

    if user_input == 1:
        new_card = random.randint(1,11)
        cards.append(new_card)
        current_total = total(cards)
        rounds += 1
        print(f"You've added {rounds} card/s")
        print(f"New Card: {new_card}")
        print(f"Total: {current_total}")

        if current_total > 21:
            print("You lose")
            break

        elif current_total == 21:
            print("You've got blackjack! You win!")
            break

    elif user_input == 2:
        print("You choose to stand")
        break

    else:
        print("Please choose a valid number! ")


# print(f" Card 1: {card_1}")
# print(f" Card 2: {card_2}")
# print(f" Sum : {sum}")

# user_input = int(input(" Enter 1 to pick a new card and 2 to stand: "))
#
# while sum < 21:
#     if user_input == 1:
#         sum = card_1 + card_2




