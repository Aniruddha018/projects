import random

mynum= random.randint(0,20)
name= input("whats your name?\n")

print("hey,"  + name +  " can you guess which number i am thinking  between 0 to 20?\n ")
usernum = int(input("enter your guess: "))

while mynum != usernum:
    if mynum > usernum:
        print("you need to guess little higher,try again")
        usernum = int(input("\n enter your guess: "))

    else:
        print("you need to guess little lower , try again")
        usernum = int(input("\n enter your guess: "))

print("congrats " + name + " you guessed the number correct , have a nice day ")        


        
