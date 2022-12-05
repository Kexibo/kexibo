'''
O(n*log(n))
Находим решение, выдаем ответ. Находим минимальную разность, а потом сравниваем все разности с прошлым ответом и записываем пары этх чисел
'''
def minimumAbsDifference(arr):
    #переменные
    arr.sort() #сортируем список
    m = 10^6 #макс значение по условию
    otv = [] #ответ

    #цикл нахождения минимальной разности
    for i in range(len(arr) - 1):
        if arr[i+1] - arr[i] < m:
            m = arr[i+1] - arr[i]
    #цикл заполнения ответа парами минимальных разностей
    for i in range(len(arr) - 1):
        if arr[i+1] - arr[i] == m:
            otv.append((arr[i], arr[i+1]))
    return otv

print(minimumAbsDifference([3,8,-10,23,19,-4,-14,27]))