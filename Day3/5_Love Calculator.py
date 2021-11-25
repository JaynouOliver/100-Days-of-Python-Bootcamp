print("Welcome to Love calculator")
name1 = input("What's your name? \n")
name2 = input("what's their name? \n")

combinedString = name2 + name1
lowecaseString = combinedString.lower()

t = lowecaseString.count("t")
r = lowecaseString.count("r")
u = lowecaseString.count("u")
e = lowecaseString.count("e")

true = t + r + u + e
l = lowecaseString.count("t")
o = lowecaseString.count("r")
v = lowecaseString.count("u")
e = lowecaseString.count("e")

love = l + o + v + e

loveScore = int(str(true + love))
if(loveScore < 10) or (loveScore > 90):
    print(f"Love Score is {loveScore}")
elif(loveScore >= 40):
    print("Score is " + loveScore)
else:
    print(f"Score is {loveScore}")


