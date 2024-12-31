santadb = []

def checkName(name):
    for x in santadb:
        if name in x:
            print("This name has already been entered.")
            return True
    return False

while True:
    name = input("Enter name to be added (enter stop to stop): ")
    if name == "stop":
        break
    if checkName(name):
        continue
    else:
        santadb.append([name])

print(santadb)
