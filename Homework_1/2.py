'''
O(n)
Всё по формулам из условия. Если четное, то делим, если не четное, то -1 и делим на 2 и переносим в новый оборот цикла
'''
def numberOfMatches(n: int) -> int:

    #Переменные счетчика и всего матчей
    x = 0
    g = 0
    while n != 1:
        if n == 1:
            f = n / 2 #Матчи в этом раунде
            x += 1 #Счётчик для принта
            print(f'- {x}st Round: Teams = {n}, Matches = {f}, and {f} team is declared the winner.')
            n = f #Кол-во команд
        else:
            if n % 2 == 0:
                f = n / 2
                x += 1
                print(f'- {x}st Round: Teams = {n}, Matches = {f}, and {f} teams advance.')
                n = f
            else:
                k = n - 1
                f = k / 2 
                h = f + 1 #Добавляем команду из прошлого тура
                x += 1
                print(f'- {x}st Round: Teams = {n}, Matches = {f}, and {h} teams advance.')
                n = h
        g += f
    return g

numberOfMatches(7)