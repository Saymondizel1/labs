class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def in_order_traversal(root):
    if root is None:
        return []
    return in_order_traversal(root.left) + [root.value] + in_order_traversal(root.right)

def build_tree_from_array(arr, i=0):
    if i < len(arr) and arr[i] is not None:
        root = BinaryTree(arr[i])
        root.left = build_tree_from_array(arr, 2 * i + 1)
        root.right = build_tree_from_array(arr, 2 * i + 2)
        return root
    return None

def build_tree_from_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read().replace(',', ' ').split()
            
            arr = []
            for item in content:
                if item.lower() in ['null','n', 'none']:
                    arr.append(None)
                else:
                    arr.append(int(item))
                    
            return build_tree_from_array(arr)
            
    except FileNotFoundError:
        print(f"Помилка: Файл '{filename}' не знайдено.")
        return None

if __name__ == "__main__":
    filename = "pyramid.txt" 
    
    print(f"Будуємо дерево з файлу {filename}...")
    root = build_tree_from_file(filename)
    
    if root:
        result = in_order_traversal(root)
        print("In-order обхід дерева:", result)