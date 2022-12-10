import math
import random
bot_choice = random.randrange(1,4)
#1 = stone
#2 = scissors
#3 = paper
if bot_choice == 1:
    bot_choice_word = "stone"
if bot_choice == 2:
    bot_choice_word = "scissors"
if bot_choice == 3:
    bot_choice_word = "paper"
gamer_choice_word = input("Please type your choice\n")
correct_choice = False
#print(bot_choice_word)
#print(gamer_choice_word)
if gamer_choice_word == "stone" and bot_choice_word == "stone":
    print(bot_choice_word)
    correct_choice = True
    print("draw")
if gamer_choice_word == "scissors" and bot_choice_word == "stone":
    print(bot_choice_word)
    correct_choice = True
    print("bot won")
if gamer_choice_word == "paper" and bot_choice_word == "stone":
    print(bot_choice_word)
    correct_choice = True
    print("gamer won")

if gamer_choice_word == "stone" and bot_choice_word == "scissors":
    print(bot_choice_word)
    correct_choice = True
    print("gamer won")
if gamer_choice_word == "scissors" and bot_choice_word == "scissors":
    print(bot_choice_word)
    correct_choice = True
    print("draw")
if gamer_choice_word == "paper" and bot_choice_word == "scissors":
    print(bot_choice_word)
    correct_choice = True
    print("bot won")

if gamer_choice_word == "stone" and bot_choice_word == "paper":
    print(bot_choice_word)
    correct_choice = True
    print("bot won")
if gamer_choice_word == "scissors" and bot_choice_word == "paper":
    print(bot_choice_word)
    correct_choice = True
    print("gamer won")
if gamer_choice_word == "paper" and bot_choice_word == "paper":
    print(bot_choice_word)
    correct_choice = True
    print("draw")

if correct_choice == False:
   print("you typed incorrect choice")