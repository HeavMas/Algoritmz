def F(root):
    stack = [(root, 0)]
    lst = []
    while stack:
        value, leng = stack.pop()
        if value.left != None:
            lst.append((value.left).val)
            stack.append((value.left, leng + 1))
        if value.right != None:
            lst.append((value.right).val)
            stack.append((value.right, leng + 1))
    min_v = 10 ** 6
    lst.append(root.val)
    lst.sort()
    for i in range(len(lst)):
        if min_v > abs(lst[i - 1] - lst[i]):
            min_v = abs(lst[i - 1] - lst[i])
    return min_v