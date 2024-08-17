class Node:
    def __init__(self, data=None):
        self.data = data
        self.next: Node|None = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def insert_at_beginning(self, data):
        new_node = Node(data)
        self.length += 1
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        self.length += 1
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

# Функція реверсування однозв'язного списку, змінюючи посилання між вузлами

    def reverse_list(self):
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev 

# Функція сортування вставками

    def insertion_sort(self):
        sorted_list = None
        current = self.head

        while current is not None:
            temp = current.next
            if sorted_list is None or sorted_list.data >= current.data:
                current.next = sorted_list
                sorted_list = current
            else:
                sorted_current = sorted_list
                while sorted_current.next is not None and sorted_current.next.data < current.data:
                    sorted_current = sorted_current.next
                current.next = sorted_current.next
                sorted_current.next = current
            current = temp
            
        self.head = sorted_list

# Функція розділення та рекурсивного сортування однозв'язного списку

    def merge_sort(self):
        if self.head is None or self.head.next is None:
            return self.head

        # Знаходимо середину списку
        slow = self.head
        fast = self.head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Розділяємо список на дві половини
        second_half = slow.next
        slow.next = None
      
        # Рекурсивно сортуємо кожну половину
        left = self.merge_sort()

        rllist = LinkedList()

        while second_half:
            rllist.insert_at_end(second_half.data)
            second_half = second_half.next

        right = rllist.merge_sort()

        # Зливаємо відсортовані половини
        self.head = self.merge(left, right)
        return self.head

# Функція об'єднання двох відсортованих списків

    def merge(self, left, right):
        dummy = Node()
        tail = dummy

        while left and right:
            if left.data <= right.data:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next

        if left:
            tail.next = left
        elif right:
            tail.next = right

        return dummy.next

llist = LinkedList()

# Вставляємо вузли в початок
llist.insert_at_beginning(5)
llist.insert_at_beginning(10)
llist.insert_at_beginning(15)

# Вставляємо вузли в кінець
llist.insert_at_end(20)
llist.insert_at_end(25)

# Друк зв'язного списку
print("\nЗв'язний список:")
llist.print_list()

# Реверсування однозв'язного списку, змінюючи посилання між вузлами
print("\nРеверсований список:")
llist.reverse_list()
llist.print_list()

# Cортування вставками
print("\nCортування вставками:")
llist.insertion_sort()
llist.print_list()

print("\nІнший зв'язний список:")


otherllist = LinkedList()

# Вставляємо вузли в початок
otherllist.insert_at_beginning(5)
otherllist.insert_at_beginning(10)
otherllist.insert_at_beginning(15)
otherllist.insert_at_beginning(6)
otherllist.insert_at_beginning(11)
otherllist.insert_at_beginning(16)

# Вставляємо вузли в кінець
otherllist.insert_at_end(-20)
otherllist.insert_at_end(-25)

otherllist.insert_at_beginning(25)
otherllist.insert_at_beginning(210)
otherllist.insert_at_beginning(215)
otherllist.insert_at_beginning(-5)
otherllist.insert_at_beginning(-10)
otherllist.insert_at_beginning(-15)
otherllist.insert_at_beginning(26)
otherllist.insert_at_beginning(211)
otherllist.insert_at_beginning(216)

otherllist.print_list()

# Сортування злиттям
print("\nСортування злиттям:")

otherllist.merge_sort()

print("Інший зв'язний посортотваний список:")

otherllist.print_list()

print("\nЗв'язний посортотваний список сортуванням вставками:")
llist.print_list()

# Злиття двох посортованих списків
print("\nЗлиття двох посортованих списків:")

merged_list = LinkedList()

merged_list.head = merged_list.merge(llist.head, otherllist.head)

merged_list.print_list()