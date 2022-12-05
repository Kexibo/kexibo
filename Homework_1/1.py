'''
O(n)
Если число четное делим на 2, если нет вычитаем 1. Успех
'''
def numberOfSteps(num: int) -> int:

        #Переменная счетчика для вывода в принтах(красиво)
        x = 1

        #цикл
        while num != 0:
            #Условие четное не четное
            if num % 2 == 0:
                #Куча переменных для вывода в принты как в примерах
                h = num // 2
                print(f'Step {x}) {num} is even; divide by 2 and obtain {h}. ')
                x =+ 1
                num = h
            else:
                h = num - 1
                print(f'Step {x}) {num} odd; subtract 1 and obtain {h}. ')
                x =+ 1
                num = h

numberOfSteps(14)