from game_data import data
from art import logo, vs
import random
count=0
accountA = random.choice(data)
accountB = random.choice(data)
from replit import clear
def continue_game():
  print(logo)
  global count
  global accountA
  global accountB
  if count>0:
    print(f"Your score is {count}")
  if accountA == accountB:
    accountB = random.choice(data)
  print(f"Compare A : {accountA['name']}, a {accountA['description']}, from {accountA['country']}")
  print(vs)
  print(f"Against B : {accountB['name']}, a {accountB['description']}, from {accountB['country']}")
  choice=input("Choose an option (A/B) :").lower()
  followersA=accountA['follower_count']
  followersB=accountB['follower_count']
  print(followersA)
  print(followersB)
  if (followersA>followersB) and (choice=='A'):
    print("You are right")
    count+=1
    clear()
    accountA=accountA
    accountB = random.choice(data)
    continue_game()
  elif (followersB>followersA) and (choice=='B'):
    print("You are right.")
    count+=1
    clear()
    accountA=accountB
    accountB = random.choice(data)
    continue_game()
  else:
    clear()
    print(f"Your score is {count}")
    print("Sorry, You are Wrong.")

continue_game()