from collections import Counter, deque


# Реализация дерева, для того чтобы конвртировать буквы в значения дерева
class HuffmanTree:
    # Узел
    class _Node:
        def __init__(self, char=None, freq=0):
            self.char = char
            self.freq = freq
            self.left = None
            self.right = None

        def __lt__(self, other):
            return self.freq < other.freq

    #
    def __init__(self):
        self._root = None
        self._nodes = {}

    def __getitem__(self, char):
        if char in self._nodes:
            return self._nodes[char]
        else:
            raise KeyError(f"Символ '{char}' не найден в кодах")

    def encode(self, text):
        if not text:
            return None
        self._build_tree(text)
        self._nodes = {}
        self._generate_nodes(self._root, "")
        return self._nodes

    def _build_tree(self, text):
        freq = Counter(text)

        nodes = [self._Node(char, count) for char, count in freq.items()]
        nodes.sort(key=lambda x: x.freq)

        queue = deque(nodes)

        while len(queue) > 1:
            left = queue.popleft()
            right = queue.popleft()

            parent = self._Node(freq=left.freq + right.freq)
            parent.left = left
            parent.right = right

            inserted = False
            for i in range(len(queue)):
                if parent.freq < queue[i].freq:
                    queue.insert(i, parent)
                    inserted = True
                    break
            if not inserted:
                queue.append(parent)
        self._root = queue[0] if queue else None

    def _generate_nodes(self, node, current_code):
        if node is None:
            return

        if node.char is not None:
            self._nodes[node.char] = current_code

        self._generate_nodes(node.left, current_code + "0")
        self._generate_nodes(node.right, current_code + "1")


# Система шифрования
class encryption_system:
    def __init__(self, file):
        self.file = open(f"{file}", "r")
        self.text = "".join(self.file.read().split())
        self.file.close()

        self.tree = HuffmanTree()
        self.isEncrypthion = False

    def encrypthion(self, gamma):
        if self.isEncrypthion:
            print("Код уже зашифрован!")
            return
        self.tree.encode(self.text)
        new_str = str()
        for i in range(len(self.text)):
            new_str += chr(1072 + int(self.tree[self.text[i]], 2) + int(gamma[i], 2))
        self.text = new_str
        self.isEncrypthion = True
        print(self.isEncrypthion)

    def decription(self, gamma):
        print(self.isEncrypthion)
        if self.isEncrypthion:
            self.isEncrypthion = False
        else:
            print("Код не зашифрован!")
            return

    def print(self):
        print(self.text)


def main():
    choise = 1
    gamma = "111111111111"
    while choise != 0:
        choise = int(
            input("""
        Введите действие->
        1) Зашифровать
        2) Расшифровать
        3) Вывод текста
        0) Выход
        Ввод: """)
        )
        system = encryption_system("./text.txt")

        match choise:
            case 1:
                system.encrypthion(gamma)
            case 2:
                system.decription(gamma)
            case 3:
                system.print()
            case 0:
                print("Выход из программы...")
                continue


if __name__ == "__main__":
    main()
