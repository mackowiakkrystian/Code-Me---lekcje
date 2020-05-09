#
# def wyszukajmaila():
#     znaleziono = ''
#     dodane = input("wprowadz emaile oddzielone przecinkiem ")
#     listamaili = dodane.split(",")
#     print(listamaili)
#     szukany = input("Podaj poszukiwany email ")
#
#     for i in listamaili:
#         if i == szukany:
#             print("TRUE")
#             znaleziono = 'y'
#     if znaleziono != 'y':
#         print("False")
#
# wyszukajmaila()




building = ['dom', 'szkola', 'kosciol', 'bar', 'szpital']
# graph = [(0, 1), (0, 2), (0, 3),
#          (1,0), (1,4),
#          (2,0), (2, 3),
#          (3,0), (3,2), (3,4),
#          (4,1), (4,3)]
# #
# for e in graph:
#     b1, b2 = e
#     print(building[b1], '--------',building[b2])

graph = [
    [0, 1, 1, 1, 0],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 1, 0],
    [1, 0, 1, 0, 1]
]

for row in range(4):
    for col in range(5):
        if graph[row][col] == 1:
            print(building[row], '------>', building[col])

