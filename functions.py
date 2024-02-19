import random

def registerCode() -> float:
    n = random.random()
    code =  2024 + n
    return code

def seeRoom():
        n = int(input('What room you want to see? '))
        funcss: dict = {
             1: see_first_room,
             2: see_second_room,
             3: see_third_room,
        }
        answer = funcss.get(n)
        answer()

def see_first_room():
    with open('FirstClass','r') as students:
        l =  students.readlines()
    print(l, end='')


def see_second_room():
    with open('SecondClass.txt', 'r') as students:
        l = students.readlines()
    print(l, end='')

def see_third_room():
    with open('ThirdClass.txt', 'r') as students:
        l =  students.readlines()
    print(l)


def createFirst(room: list):
    room.sort()
    for k in room:
        with open('FirstClass.txt', 'a') as sala:
            sala.write(str(k))


def createSecond(room: list):
    room.sort()
    for k in room:
        with open('SecondClass.txt', 'a') as sala:
            sala.write(str(k))


def createThird(room: list):
    room.sort()
    for k in room:
        with open('ThirdClass.txt', 'a') as sala:
            sala.write(str(k))