from functions import *

def register():
        student = list()
        while True:
            student.clear()
            name = str(input('Student name: ')).upper()
            student.append(name)
            
            register_code = registerCode()
            student.append(register_code)
            
            room = str(input('Wanted class room: ')).upper()[0]
            if room in 'FIRST':
                first_year.append(student.copy())
                
                
            elif room in 'SECOND':
                second_year.append(student.copy())
                
            elif room in 'THIRD':
                third_year.append(student.copy())
                

            
            
            while True:
                resp = str(input('Quer continuar? [S/N]')).upper()[0]
                if resp in 'SN':
                    break
                print('ERRO"! responda apenas S ou N.')
            if resp == 'N':
                createClass()
                break

def createClass():
     createFirst(first_year)
     createSecond(second_year)
     createThird(third_year)

first_year = list()
second_year = list()
third_year = list()




print('='*50)
print('Select one of this options: \n'
      'To register  [1] \n'
      'See class room [2] \n')
print('='*50)

choices = int(input('Your choice: '))

funcs: dict = {
    1: register,
    2: seeRoom,
    
}

final = funcs.get(choices)
final()



print(first_year)
print(second_year) 
print(third_year)
