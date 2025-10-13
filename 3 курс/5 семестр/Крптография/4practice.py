class task:
    def __init__(self, gamma):
        self.letter_dict = dict()
        self.gamma = gamma
    def create_dict_alf(self):
        letters = [chr(i) for i in range(1072, 1104) if chr(i) not in ['ъ', 'ё', 'й']]
        self.letter_dict['я'] = 0
        for i, letter in enumerate(letters, 1):
            if(letter != 'я'):
                self.letter_dict[letter] = i
    def gamma_print(self):
        for value in self.gamma:
            print(value)
    def display_aligned_dict(self, columns=20, cell_width=4):
        items = list(self.letter_dict.items())
        
        for i in range(0, len(items), columns):
            row_items = items[i:i + columns]


            key_cells = []
            value_cells = []
            for key, value in row_items:
                key_cells.append(f" {key} ".center(cell_width))
                value_cells.append(f" {value} ".center(cell_width))
            
            print("|".join(key_cells))
            print("|".join(value_cells))

            if i + columns < len(items):
                self.gamma_print()
                separator = "+".join(["-" * cell_width for _ in row_items])
                print(separator)
        self.gamma_print()


def main():
    task3 = task(['З','И','Я','Т'])
    task3.create_dict_alf()
    task3.display_aligned_dict()

if __name__ == "__main__":
    main()


