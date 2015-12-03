# testi dialog treetä varten jos npc jne..


def toimiiko():
    conta = 0
    print("abc?")
    print("a")
    print("b")
    print("c")
    while True:
        answer = input()
        answer = answer.lower()
        if answer in ['a', 'b', 'c', 'd', 'quit']:
            break
        print("Please input a, b, c or d.")
    if answer == 'a':
        print("a:bc?")
        print("b")
        print("c")
        while True:
            answer = input()
            answer = answer.lower()
            if answer in ['a', 'b', 'c', 'd', 'quit']:
                break
            print("Please input a, b, or c.")
        if answer == 'a':
            print("b")
            input("blabla")
        if answer == 'b':
            print("c")
            input("blabla")
        if answer in ['c', 'd', 'quit']:
            return
        conta = 1

    elif answer == 'b':
        print("b:ac?")
        print("a")
        print("c")
        while True:
            answer = input()
            answer = answer.lower()
            if answer in ['a', 'b', 'c', 'd', 'quit']:
                break
            print("Please input a, b, or c.")
        if answer == 'a':
            print("a")
            input("blabla")
        if answer == 'b':
            print("c")
            input("blabla")
        if answer in ['c', 'd', 'quit']:
            return
        conta = 1
    elif answer == 'c':
        print("c:ab?")
        print("a")
        print("b")
        while True:
            answer = input()
            answer = answer.lower()
            if answer in ['a', 'b', 'c', 'd', 'quit']:
                break
            print("Please input a, b, or c.")
        if answer == 'a':
            print("a")
            input("blabla")
        if answer == 'b':
            print("b")
            input("blabla")
        if answer in ['c', 'd', 'quit']:
            return
        conta = 1
    else:
        print("")

    if conta == 1:
        print("abc?")
        print("a")
        print("b")
        print("c")
        while True:
            answer = input()
            answer = answer.lower()
            if answer in ['a', 'b', 'c', 'd', 'quit']:
                break
            print("Please input a, b, c or d.")
        if answer == 'a':
            print("a:bc?")
            print("b")
            print("c")
            while True:
                answer = input()
                answer = answer.lower()
                if answer in ['a', 'b', 'c', 'd', 'quit']:
                    break
                print("Please input a, b, or c.")
            if answer == 'a':
                print("b")
                input("blabla")
            if answer == 'b':
                print("c")
                input("blabla")
            if answer in ['c', 'd', 'quit']:
                return
            conta = 2
        elif answer == 'b':
            print("b:ac?")
            print("a")
            print("c")
            while True:
                answer = input()
                answer = answer.lower()
                if answer in ['a', 'b', 'c', 'd', 'quit']:
                    break
                print("Please input a, b, or c.")
            if answer == 'a':
                print("a")
                input("blabla")
            if answer == 'b':
                print("c")
                input("blabla")
            if answer in ['c', 'd', 'quit']:
                return
            conta = 2
        elif answer == 'c':
            print("c:ab?")
            print("a")
            print("b")
            while True:
                answer = input()
                answer = answer.lower()
                if answer in ['a', 'b', 'c', 'd', 'quit']:
                    break
                print("Please input a, b, or c.")
            if answer == 'a':
                print("a")
                input("blabla")
            if answer == 'b':
                print("b")
                input("blabla")
            if answer in ['c', 'd', 'quit']:
                return
            conta = 2
        else:
            print("")

    if conta == 2:
        print(conta)
    return
