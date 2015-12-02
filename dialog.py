# testi dialog treetä varten jos npc jne..


print("")
print("")
print("")
print("")
while True:
    answer = input()
    answer = answer.lower()
    if answer in ['a', 'b', 'c', 'd', 'quit']:
        break
    print("Please input a, b, c or d.")
if answer == 'a':
    print("a")
    print("")
    print("")
    while True:
        answer = input()
        answer = answer.lower()
        if answer in ['a', 'b', 'c', 'd', 'quit']:
            break
        print("Please input a, b, or c.")
    if answer == 'a':
        print("b")
        input("blabla")
    elif answer == 'b':
        print("c")
        input("blabla")
    else:
        print("")
elif answer == 'b':
    print("b")
    print("")
    print("")
    while True:
        answer = input()
        answer = answer.lower()
        if answer in ['a', 'b', 'c', 'd', 'quit']:
            break
        print("Please input a, b, or c.")
    if answer == 'a':
        print("a")
        input("blabla")
    elif answer == 'b':
        print("c")
        input("blabla")
    else:
        print("")
elif answer == 'c':
    print("c")
    print("")
    print("")
    while True:
        answer = input()
        answer = answer.lower()
        if answer in ['a', 'b', 'c', 'd', 'quit']:
            break
        print("Please input a, b, or c.")
    if answer == 'a':
        print("a")
        input("blabla")
    elif answer == 'b':
        print("b")
        input("blabla")
    else:
        print("")
else:
    print("")
