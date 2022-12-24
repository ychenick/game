import random
print("hello, this is a Kata game\n")
print("it's pretty dumb, but well...\n")
pocket_money = 500
emotions = ["cool!", "so-so", "bad"]
days = ["Monday", "Tuesday", "Wednessday", "Thursday", "Friday", "Saturday", "Sunday"]
for theday in days:
    if theday=="Monday":
        print("It is ", theday, "and you need to go to school");
        pocket_money = pocket_money + 300 # your mom gave you that for school lunch
        pocket_money = pocket_money - 210 # the actual price of the lunch
    if theday=="Tuesday":
        print("It is ", theday, "and you need to go to school");
        pocket_money = pocket_money + 300 # your mom gave you that for school lunch
        pocket_money = pocket_money - 210 # the actual price of the lunch
    if theday=="Wednessday":
        print("It is ", theday, "and you need to go to school");
        pocket_money = pocket_money + 300 # your mom gave you that for school lunch
        pocket_money = pocket_money - 210 # the actual price of the lunch
    if theday=="Thursday":
        print("It is ", theday, "and you need to go to school");
        pocket_money = pocket_money + 300 # your mom gave you that for school lunch
        pocket_money = pocket_money - 210 # the actual price of the lunch
    if theday=="Friday":
        print("It is ", theday, "and you need to go to school");
        pocket_money = pocket_money + 300 # your mom gave you that for school lunch
        pocket_money = pocket_money - 210 # the actual price of the lunch
    if theday=="Saturday":
        print("It is ", theday)
        going_to_cinema = input("Would like you to go to a cinema?\nPlease, type yes or no\n")
        if going_to_cinema=="yes":
            pocket_money = pocket_money - 300
            your_emotion_number = random.randrange(0,3)
            your_emotion = emotions[your_emotion_number]
            print("you watched the movie, it was ", your_emotion)
        elif going_to_cinema=="no":
            print("you spent whole saturday coding the games")
        else:
            print("sorry, I didn't understand you!")
    if theday=="Sunday":
        print("It is ", theday)
        going_to_park = input("Would like you to walk to a park?\nPlease, type yes or no\n")
        if going_to_park=="yes":
            pocket_money = pocket_money - 300
            your_emotion_number = random.randrange(0,3)
            your_emotion = emotions[your_emotion_number]
            print("you walk in the park, it was ", your_emotion)
        elif going_to_park=="no":
            print("you spent whole sunday coding the games")
        else:
            print("sorry, I didn't understand you!")
print("you survived the week!")
print("you have this amount of money", pocket_money)