from random import randint

santadb = []

def checkName(name):
    for x in santadb:
        if name in x:
            print("This name has already been entered.")
            return True
    return False

def assignPerson():
    possible = []
    for i in range(0,len(santadb)):
        possible.append(i)
    for x in santadb:
        randchoice = randint(0,len(possible)-1)
        x.append(possible[randchoice])
        possible.pop(randchoice)
    print("🎅 Here are your pairings: ")
    for x in santadb:
        print(x[0] + " gives a gift to " + santadb[x[1]][0])

while True:
    name = input("Enter name to be added (enter stop to stop): ")
    if name == "stop":
        break
    if checkName(name):
        continue
    else:
        santadb.append([name])


assignPerson()
