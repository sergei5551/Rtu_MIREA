from collections import Counter, deque


class HuffmanTree:
    class _Node:
        def __init__(self, char=None, freq=0):
            self.char = char
            self.freq = freq
            self.left = None
            self.right = None

        def __lt__(self, other):
            return self.freq < other.freq

    def __init__(self):
        self._root = None
        self._codes = {}  # символ -> код
        self._reverse_codes = {}  # код -> символ

    def __getitem__(self, char):
        if char in self._codes:
            return self._codes[char]
        else:
            raise KeyError(f"Символ '{char}' не найден в кодах")

    def encode(self, text):
        if not text:
            return None
        self._build_tree(text)
        self._codes = {}
        self._reverse_codes = {}
        self._generate_codes(self._root, "")
        return self._codes

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

    def _generate_codes(self, node, current_code):
        if node is None:
            return

        if node.char is not None:
            self._codes[node.char] = current_code
            self._reverse_codes[current_code] = node.char

        self._generate_codes(node.left, current_code + "0")
        self._generate_codes(node.right, current_code + "1")

    def get_char_by_code(self, code):
        """Найти символ по коду Хаффмана"""
        return self._reverse_codes.get(code)


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

        try:
            self.tree.encode(self.text)
            new_str = ""
            for i in range(len(self.text)):
                huffman_code = self.tree[self.text[i]]
                encrypted_char_code = (
                    1072 + int(huffman_code, 2) + int(gamma[i % len(gamma)], 2)
                )
                new_str += chr(encrypted_char_code)
            self.text = new_str
            self.isEncrypthion = True
            print("Шифрование завершено")
        except Exception as e:
            print(f"Ошибка при шифровании: {e}")

    def decription(self, gamma):
        if():

        if not self.isEncrypthion:
            print("Код не зашифрован!")
            return
        try:
            new_str = ""
            for i in range(len(self.text)):
                encrypted_char_code = ord(self.text[i])
                huffman_code_int = (
                    encrypted_char_code - 1072 - int(gamma[i % len(gamma)], 2)
                )

                huffman_code = bin(huffman_code_int)[2:]

                original_char = self.tree.get_char_by_code(huffman_code)
                # Для ведущих нулей
                if original_char is None:
                    for length in range(1, 10):
                        padded_code = huffman_code.zfill(length)
                        original_char = self.tree.get_char_by_code(padded_code)
                        if original_char is not None:
                            break

                if original_char is not None:
                    new_str += original_char
                else:
                    print(f"Не удалось расшифровать символ с кодом {huffman_code}")
                    new_str += "?"  # символ-заглушка

            self.text = new_str
            self.isEncrypthion = False
            print("Дешифрование завершено")

        except Exception as e:
            print(f"Ошибка при дешифровании: {e}")

    def print(self):
        print(self.text)


def main():
    choise = 1
    gamma = "111111111111"
    system = encryption_system("./text.txt")

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
