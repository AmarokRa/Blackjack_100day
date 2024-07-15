from logo_Blackjack import logo 
import random

  
def calculate_score(hand):
  score = sum(hand)
  if score > 21 and 11 in hand:
    hand.remove(11)
    hand.append(1)
  score = sum(hand)
  return score

user_cards = []

computer_cards = []

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] 


def blackjack():
  print(logo)

  play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
  if play_game != 'y':
    return
     
  user_cards.extend([random.choice(cards) for _ in range(2)])
  computer_cards.extend([random.choice(cards) for _ in range(2)])

  game_over = False

  while not game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your cards: {user_cards}, current score: {user_score}.")
    print(f"Computer cards: {computer_cards[0]}, current score: {computer_score}.")
  
    if computer_score == 21:
      print("Blackjack! \n You lose!")
      game_over = True

    elif user_score == 21:
      print("Blackjack! \n You winn!")
      game_over = True
  
    elif user_score == 21 and computer_score == 21:
      print("Blackjack! \n You lose!") 
      game_over = True

    else:
      another_card = input("Type 'y' to get another card, type 'n' to pass: ")
      if another_card == 'y':
        user_cards.append(random.choice(cards))
      else: 
        game_over = True

  
  user_score = calculate_score(user_cards)
  computer_score = calculate_score(computer_cards)
  while computer_score != 21 and computer_score < 19:
    computer_cards.append(random.choice(cards))
    computer_score = calculate_score(computer_cards)
 
  print(f"Your final hand: {user_cards}, final score: {user_score}")
  print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")

  
  if user_score > 21:
    print("You lose!")
  
  elif computer_score > 21:
    print("You win !")

  elif user_score == computer_score:
    print("It's a Draw !")
    
  elif user_score > computer_score:
    print("You win !")

  else:
    print("You lose !")

  replay = input("Do you want to play again? Type 'y' or 'n': ")
  if replay != 'y':
    game_over = True
    

blackjack()