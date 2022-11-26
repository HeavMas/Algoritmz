
def F(n):
    arr = [0] * (n + 1)
    arr[0] = 0
    arr[1] = 1
    for i in range(1, len(arr)):
        if 2 <= 2 * i <= n:
            arr[2 * i] = arr[i]
        if 2 <= 2 * i + 1 <= n:
            arr[2 * i + 1] = arr[i] + arr[i + 1]
    return arr[-1]


print(F(2))
