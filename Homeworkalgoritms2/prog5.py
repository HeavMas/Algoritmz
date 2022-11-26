#Создаётся переменная в которой записывается длинна списка(минимальное кол-во дней в ответе), далее заполняем стеки каждый раз внутри стэка прогоняем считающий кол-во элементов внутри
#Если последовательность не соблюдается стэк пустой
#Сложность O(N^2)
def stock(arr):
    count = len(arr)
    stack = []
    for i in range(len(arr)):
        if arr[i - 1] > arr[i] and arr[i - 1] - arr[i] == 1:
            stack.append(arr[i - 1])
            if len(stack) > 2:
                for i in range(len(stack)):
                    count += 1
        else:
            stack.clear()
    return count


print(stock([3, 2, 1, 4]))