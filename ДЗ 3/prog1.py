#Сложность O(n).Цикл while проходится по всем значениям списка и добавляет их в строку. Сравниваем строку и обратную ей строку

def F(head):
    back_head = ''
    while head:
        back_head += str(head.val)
        head = head.next
    return back_head == back_head[::-1]