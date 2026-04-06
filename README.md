# lab4
# Repository for labs Laboratory Work: Priority Queue (Doubly Linked List Implementation)

## Task Description
This laboratory work implements a Priority Queue data structure from scratch using a custom Doubly Linked List. 

## Problem Statement
* A priority queue must manage elements based on their assigned priority values.
* Elements with a higher priority value must be dequeued before elements with a lower priority.
* If multiple elements have the same priority, they should be processed in the order they were added (FIFO - First-In-First-Out).
* The data structure must be built using a doubly linked list, meaning each node contains pointers to both the previous and the next nodes.
* The queue must support standard operations: inserting elements, extracting the maximum priority element, peeking at the maximum element, and displaying the queue.

## Objective
Implement the `Node` and `PriorityQueue` classes with the following core functions:
1.  `insert(value, priority)`: Inserts a new node in the correct position to maintain descending priority order.
2.  `extract_max()`: Removes and returns the element with the highest priority.
3.  `peek()`: Returns the element with the highest priority without removing it.
4.  `is_empty()`: Checks if the queue is empty.
5.  `display()`: Returns a string representation of the queue.

## Algorithm Overview
This implementation relies on maintaining a sorted doubly linked list:
1.  **Node Structure**: Each node stores a `value`, a `priority`, a `prev` pointer, and a `next` pointer.
2.  **Insertion**: 
    * If the queue is empty, the new node becomes both the `head` and `tail`.
    * If the new node has a higher priority than the `head`, it becomes the new `head`.
    * Otherwise, the algorithm traverses the list from the `head` to find the first node with a strictly lower priority. The new node is inserted immediately before this node, ensuring stable sorting (FIFO for equal priorities).
    * If the end of the list is reached, the new node becomes the `tail`.
3.  **Extraction/Peek**: Since the list is kept sorted in descending order of priority, the highest priority element is always at the `head`. These operations simply access or remove the `head` node.

## Full Solution

```python
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
