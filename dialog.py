# testi dialog treetä varten jos npc jne..
import textwrap

def wrap(text):
    print(textwrap.fill(text, 80))

def talkShaman():
    while True:
        while True:
            wrap("Shaman: \"Hello stranger.\"")
            wrap("a) Who are you?")
            wrap("b) Do you know who I am?")
            wrap("q) I should go now.")
            answer = input()
            answer = answer.lower()
            if answer in ['a', 'b', 'q', 'quit']:
                break
        if answer == 'a':
            wrap("Shaman: \"I am a shaman.\"")
            print("")
        if answer == 'b':
            wrap("Shaman: \"No but I have something that may help you remember. Just gather me some herbs and I'll make you potion of endless memory.\"")
            print("")
        if answer in ['q', 'quit']:
            break

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