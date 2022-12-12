# Сложность O(n), n - Количество вершин дерева. Сначало делаем обход и смотрим максимальную глубину и делаем список, равный по максимальному числу(т.е) находяшемуся в самом низу.
#Далее еще один обход в котором мы в список элементы, и в другой список текущюю длинну. В последнем цикле в новый список мы добавляем среднее значение.

def F(root):
    stack = [(root, 0)]
    deep = []
    k = [0] * max(deep)
    For_print = [0] * max(deep)
    Final_ans = [0] * max(deep)
    while stack:
        value, leng = stack.pop()
        if value.left == None and value.right == None:
            deep.append(leng + 1)
        if value.left != None:
            stack.append((value.left, leng + 1))
        if value.right != None:
            stack.append((value.right, leng + 1))
    stack = [(root, 0)]
    while stack:
        value, leng = stack.pop()
        Final_ans[leng] += value.val
        k[leng] += 1
        if value.left != None:
            stack.append((value.left, leng + 1))
        if value.right != None:
            stack.append((value.right, leng + 1))

    for i in range(len(Final_ans)):
        For_print[i] = Final_ans[i] / k[i]

    return Final_ans
