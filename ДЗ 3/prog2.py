#Сложность  O(n). Записываем в строку все значения, и смотрим как будет выглядить число в двоичной записи

def F(head):
    value = ''
    while head:
        value += str(head.val)
        head = head.next
    return int(value, 2)
