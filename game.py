import random
from art import logo

# play = input("Do you want to play a game? Type 'yes' or 'no' ").lower()
# if play == "yes":
print(logo)

cards = [11, 2, 3,4,5,6,7,8,9,10,10,10,10]
def ace(hand):
  if 11 in hand and sum(hand)>21:
    hand.remove(11)
    hand.append(1)
  return hand

your_cards = []
computer_cards = []
for i in range(2):
    your_cards.append(random.choice(cards))
for i in range(2):
    computer_cards.append(random.choice(cards))
your_cards = ace(your_cards)
computer_cards = ace(computer_cards)
print(f"Your cards are {your_cards}")
print(f"Computer's first card is {computer_cards[0]}")

def deal_card(your_cards):
  deal = input("Type 'y' to get another card, type 'n' to pass: ").lower()
  if deal == "y":
      your_cards.append(random.choice(cards))
      your_cards = ace(your_cards)
      print(f"Your cards are {your_cards}")
      return deal_card(your_cards)
  elif deal == "n":
      return your_cards
  else:
      print("Invalid input")
      return deal_card(your_cards)
your_cards = deal_card(your_cards)
my_points = sum(your_cards)
computer_points = sum(computer_cards)
while computer_points < 17:
  computer_cards.append(random.choice(cards))
  computer_cards =ace(computer_cards)
  computer_points = sum(computer_cards)
print(f"Your final hand is {your_cards}")
print(f"Computer's final hand is {computer_cards}")
print(f"Your final points is {my_points}")
print(f"Computer's final points is {computer_points}")

if my_points == 21:
  print("You win")
elif my_points > 21:
  print("You lose")
elif computer_points == 21:
  print("You lose")
elif computer_points > 21:
  print("You win")
elif my_points > computer_points:
  print("You win")
elif computer_points > my_points:
  print("You lose")
elif my_points == computer_points:
  print("Draw")