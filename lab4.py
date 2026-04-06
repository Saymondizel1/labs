

class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
        self.prev = None
        self.next = None

class PriorityQueue:
    def __init__(self):
        self.head = None
        self.tail = None
    def is_empty(self):
        return self.head is None

    def insert(self, value, priority):
        new_node = Node(value, priority)

        if self.is_empty():
            self.head = self.tail = new_node
            return
        
        if priority > self.head.priority:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            return

        current = self.head
        while current is not None and current.priority >= priority:
            current = current.next
        if current is None:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        else:
            new_node.prev = current.prev
            new_node.next = current
            if current.prev:
                current.prev.next = new_node
            current.prev = new_node

    def extract_max(self):
        if self.is_empty():
            raise IndexError("Черга порожня. Неможливо видалити елемент.")

        removed_node = self.head
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        else:
            self.head.prev = None

        return removed_node.value, removed_node.priority

    def peek(self):
        if self.is_empty():
            raise IndexError("Черга порожня. Немає елементів для перегляду.")
        
        return self.head.value, self.head.priority

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(f"['{current.value}', prio: {current.priority}]")
            current = current.next
        return " -> ".join(elements)

if __name__ == "__main__":
    pq = PriorityQueue()

    print("Додаємо елементи...")
    pq.insert("Завдання A (Низький)", 1)
    pq.insert("Завдання B (Високий)", 5)
    pq.insert("Завдання C (Середній)", 3)
    
    pq.insert("Завдання D (Високий - друге)", 5) 
    pq.insert("Завдання E (Високий - третє)", 5)

    print("\nПоточний стан черги:")
    print(pq.display())
    print(f"\nПерегляд (Peek): {pq.peek()}")
    print("\nВидаляємо елементи по черзі:")
    while not pq.is_empty():
        val, prio = pq.extract_max()
        print(f"Виконано: '{val}' з пріоритетом {prio}")