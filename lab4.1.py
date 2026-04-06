from lab4 import PriorityQueue

class ExtendedPriorityQueue(PriorityQueue):
    def change_priority(self, value, new_priority):
        current = self.head
        while current is not None:
            if current.value == value:
                break
            current = current.next
            
        if current is None:
            print(f"Помилка: Елемент '{value}' не знайдено.")
            return
        if current.prev is not None:
            current.prev.next = current.next
        else:
            self.head = current.next 
            
        if current.next is not None:
            current.next.prev = current.prev
        else:
            self.tail = current.prev 

        self.insert(value, new_priority)


if __name__ == "__main__":
    pq = ExtendedPriorityQueue()

    print("--- 1. Початкове наповнення черги ---")
    pq.insert("Фонова задача", 1)
    pq.insert("Оновлення системи", 3)
    pq.insert("Запит користувача", 5)
    
    print("Поточний стан черги:")
    print(pq.display())
    print("\n--- 2. Зміна пріоритету ---")
    print("Ситуація: 'Фонова задача' стала критично важливою (пріоритет 10)!")
    pq.change_priority("Фонова задача", 10)
    print("\nСтан черги ПІСЛЯ зміни пріоритету:")
    print(pq.display())

    print("\n--- 3. Перевірка видалення ---")
    val, prio = pq.extract_max()
    print(f"Зараз виконується: '{val}' з пріоритетом {prio}")