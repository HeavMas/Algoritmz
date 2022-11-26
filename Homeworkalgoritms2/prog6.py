#Сложность O(log(n)). Возможно лишь 2 пути сбора макс прибыли, либо 0ой эл списка, 2ой и т.д, либо 1ый, 3ий и тд. Это если элементов больше 3х
#Иначе это просто мак элемент из списка
def rob(arr):
    if len(arr) > 3:
        cash1 = 0
        cash2 = 0
        for i in range(0, len(arr), 2):
            cash1 += arr[i]
        for i in range(1, len(arr), 2):
            cash2 += arr[i]
        return max(cash1, cash2)
    else:
        return max(arr)


print(rob([2, 3, 2]))