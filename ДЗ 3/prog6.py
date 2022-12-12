#Сложность алгоритма O(log(n)). Создаём 2 связанных списка в одном будем делать 1 шаг в другом сразу 2, если в какой-то момент значения станут равны - есть цикл
def F(head):
    head1 = head
    head2 = head
    while head2 != None and head2.next != None:
        head1 = head1.next
        head2 = head2.next.next
        if head1 == head2:
            return True
    return False