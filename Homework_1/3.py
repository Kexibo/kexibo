'''
O(n^2)
Проверяем в списке первую букву и вторую. Тут всё очевидно)
'''
def numJewelsInStones(jewels: str, stones: str) -> int:

    #Переменная ответа
    x=0

    #Цикл алфавита
    for i in jewels:
        #Цикл набора букв каких-то
        for j in stones:
            #если такая буква есть добавляем в ответ
            if i == j:
                x += 1
    return x

print(numJewelsInStones("aA","aAAbbbb"))