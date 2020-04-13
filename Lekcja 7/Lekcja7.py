# import sys
#
# print(sys.platform)
#
# if sys.platform == 'win32':
#     print("Windows")
# elif sys.platform == 'darwin':
#     print("Mac")
# elif 'linux' in system.platform: # bo bedzie albo linux 1 albo linux2
#     print("Linux")
# else:
#     print("inny system")


def find_longest_word(sequence):
    """Finds the longest element in a sequence"""
    longest_word = ''
    for word in sequence:
        if len(word) > len(longest_word):
            longest_word = word

    return longest_word

word = "Abraca"
print(find_longest_word(word))


#ZADANIE NR 3
# import file_helper as fh
#
# txt = fh.safe_open('nadwaga.txt')
# print(txt)
# txt_to_save = 'nanananana\t ssadasda'
# fh.safe_save('testowyplik.txt', txt_to_save)


#ZADANIE 5
import file_helper as pola

room1 = pola.square(4)
room2 = pola.rectangle(3, 5)
room3 = pola.triangle(4, 9)

sum_room = room1 + room2 + room3

print(sum_room)

#ZADANIE6
slowo = "abcdks2222s"
poprzednie = ''
najwiecej = ''
licznik = 1
for i in slowo:
    if i == poprzednie:
        poprzednie = i
        najwiecej = i
        licznik += 1
    else:
        poprzednie = i
        najwiecej = i

print(licznik)
print(najwiecej)