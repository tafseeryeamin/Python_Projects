import random

while True:
    action_1 = input("If you want to play press y, if you want to quit press n: ").lower()
    if "y" in action_1:
        # Define card values
        card_values = {
            "J": 10,
            "Q": 11,
            "K": 12,
            "A": 1
        }
        cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, "J", "Q", "K"]


        player_card1 = random.choice(cards)
        player_card2 = random.choice(cards)
        dealer_card1 = random.choice(cards)
        dealer_card2 = random.choice(cards)

        print(f'Your two cards are {player_card1}, {player_card2}')
        print(f"Dealer's cards are {dealer_card1}, [Hidden]")

        # Convert card values to numbers
        def get_card_value(card):
            return card_values.get(card, card)

        player_total = get_card_value(player_card1) + get_card_value(player_card2)
        dealer_total = get_card_value(dealer_card1) + get_card_value(dealer_card2)

        print(f"Your total value: {player_total}")

        # Player's turn to draw cards
        while player_total < 21:
            next_move = input("Are you ready for your next card? (press 'y' to play, anything else to quit): ").lower()
            if next_move == "y":
                player_card3 = random.choice(cards)
                player_total += get_card_value(player_card3)
                print(f"Your next card is {player_card3}")
                print(f"Your new total value: {player_total}")
            else:
                break

        # Dealer's turn to draw cards (dealer hits until total is at least 17)
        while dealer_total < 17:
            dealer_card3 = random.choice(cards)
            dealer_total += get_card_value(dealer_card3)
            print(f"Dealer draws a card: {dealer_card3}")
            print(f"Dealer's total value: {dealer_total}")

        # Determine the winner
        print(f"Your final total: {player_total}")
        print(f"Dealer's final total: {dealer_total}")

        if player_total > 21 and dealer_total > 21:
            print("No one wins! Both you and the dealer busted.")
        elif player_total > 21:
            print("You bust!")
        elif dealer_total > 21:
            print("Dealer busts!")
        elif player_total == dealer_total:
            print("It's a tie!")
        elif player_total > dealer_total:
            print("You win!")
        else:
            print("Dealer wins!")

        # Ask if the user wants to play again
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != "y":
            print("Thank you for playing!")
            break  # Exit the outer loop and end the program
    elif "n" in action_1:
        print("Thank you for visiting the website")
        break  # Exit the outer loop and end the program
    else:
        print("Press y or n")