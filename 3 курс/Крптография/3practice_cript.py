import textwrap
import copy
def replace_char_cript(list_2_char, repace_elements):

    len_colums = len(list_2_char[0])
    len_rows = len(list_2_char)
    new_list = copy.deepcopy(list_2_char)
    for i in range(len_rows):
        for j in range(len(repace_elements)):
            new_list[i][j] = list_2_char[i][repace_elements[j]-1]
    print([str(i+1) for i in range(len_colums)])
    print([str(repace_elements[i]) for i in range(len(repace_elements))], end="\n\n")
    for row in new_list:
        print(row)


def main():
    code = textwrap.dedent("""
    ЛЗЕНАЕААВРНААСИНЬМВ
    РТОПЕИКАЯЧЛЧЕААНДЕА
    ОУКИШППЕЕААЛВОЛРДАГ
    ОИЛЕОУЕСГКМЦЧКОЛРОВ
    МТАВОУУРТООЫКОТЛДЕО
    ОБУГАВГЕЕИНКВОШТЦИВ
    КНИХАЩИИЕРДАИНОКАДН
    ИВИЛАДПЯАРВЫБРОВИРМ
    ОДОРБЬЧИДЖНУАЕЕОНШЕ
    НЛГАЛОЕНДООАНСЕИВЗА
    ВАЛАХЗСАДСННСЕЫЫВШИ
    """)
    list_1_char = list()
    list_2_char = list()
    for char in code[1:]:
        if(char == '\n'):
            list_2_char.append(list_1_char)
            list_1_char = list()
            continue
        list_1_char.append(char)
    repace_elements = [13, 10, 15, 11, 8, 19, 1, 7, 14, 17, 6, 9, 16, 5, 4, 3, 2, 12, 18]
    replace_char_cript(list_2_char, repace_elements) # Заменяет и выводит буквы


if "__main__" == __name__:
    main()
"""
    [13, 10, 15, 11, 8, 19, 1, 7, 14, 17, 6, 9, 16, 5, 4, 3, 2, 12, 18]
"""