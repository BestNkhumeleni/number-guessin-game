import random

num =  random.randint(0,100)

guess = eval(input("guess a number between 1 and 99:\n"))

while True:  
    if num == guess:
        print("you must be a prophet because gawd daym")
        print("unless it took you more thab one try in which case, get good bro")
        break
    elif num-5<guess and guess<num+5:
        print("prety damn close you are only about 5 off")
    elif num-10<guess and guess<num+10:
        print("prety damn close you are only about 10 off")
        print("Not quite as close as being 5 off though im just say")
    elif num-30<guess and guess<num+30:
        print("not even remotely close, lol")
    elif num-50<guess and guess<num+50:
        print("I think you should probably just give up, its okay, you,ll get the next one")    
    elif num-100<guess and guess<num+100:
        print("Yoh")
    print()
    guess = eval(input("One more time guess a number between 1 and 99:\n"))
        