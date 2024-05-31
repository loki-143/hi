#Hangman Game to Guess the names of Fruits.
import random
name=["apple","banana","orange",'grape','melons',"mango"]
list1=list(random.choice(name))
print("Lets Play Hangman")
list2=[]
stop=6
for i in list1:
    list2+='_'
print("You have 6 Lives. Try to Guess")
print(list2)
while True:
    char=input("Guess a Letter:")

    if char in list1:
        for j in range(len(list1)):
            if char==list1[j]:
                break
        list2[j]=char
        list1[j]='_'
        print("Right Guess")
        print(list2)
    else:
        stop-=1
        print(f"You have Guessed Wrong Word and you have {stop} Lives")
    if('_' not in list2):
        print("YOU WON!")
        break
    if(stop==0):
        print(list2)
        print("You Lost")
        break



