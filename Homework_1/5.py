'''
O(n)
Мы добавляем скобки и удаляем их когда они закрываются, а когда закрываются скобки второго уровня опустошается список
 и после этого мы добавляем то что было в этих скобках в ответ. Победа!
'''
def g(S):

    #Создаю строку для ответа, переменную для индексов и список для их хранения
    otv = ""
    i = 0
    stack = []
    
    #Начинаю цикл 
    while i<len(S):
        if S[i] == '(':
            stack.append(i)
        elif S[i] == ')':
            index_remove = stack.pop()
            #если у нас в списке становится пусто, значит это были скобки второго уровня
            if not stack:
                #добавляем в ответ то что было в тех скобках
                otv += S[index_remove+1:i]
        i+= 1
    return otv
print(g("(()())(())"))