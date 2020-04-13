def safe_open(file_name):
    with open(file_name) as f:
        content = f.read()
    return content

def safe_save(file_name, content):
    with open(file_name, 'x') as f:
        f.write(content)
    print('zapisano')


def square(a):
    return a*a

def rectangle(a, b):
    return a * b

def triangle(a,h):
    return a * h * 0.5

#Kolejne zadanie 6
def longest_in_seq(sequence):
    longest_substr = ''
    tmp_substr = ''
    for id, letter in enumerate(sequence):
        if id > 0:
            if letter == sequence[id-1]:
                tmp_substr += letter
            else:
                if len(tmp_substr) > len(longest_substr):
                    longest_substr = tmp_substr
                tmp_substr = letter
        else:
            longest_substr = letter
            tmp_substr = letter
    return longest_substr, len(longest_substr)



txt, lenght = longest_in_seq("babanannnnnnann")
print("Statystyki dla slowa, dl:", txt, lenght)