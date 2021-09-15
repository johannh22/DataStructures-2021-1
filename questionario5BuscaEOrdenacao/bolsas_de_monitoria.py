def quick_sort(lista):
    quick_sort_helper(lista, 0, len(lista) - 1)

def quick_sort_helper(lista, primeiro, ultimo):
    if primeiro < ultimo:

        part = particionar(lista, primeiro, ultimo)

        quick_sort_helper(lista, primeiro, part - 1)
        quick_sort_helper(lista, part + 1, ultimo)

def particionar(lista, primeiro, ultimo):
    pivo = lista[primeiro]

    esquerda = primeiro + 1
    direita = ultimo

    terminou = False
    while not terminou:

        while esquerda <= direita and lista[esquerda] <= pivo:
            esquerda += 1

        while direita >= esquerda and lista[direita] >= pivo:
            direita -= 1
        
        if direita < esquerda:
            terminou = True
        else:
            tmp = lista[esquerda]
            lista[esquerda] = lista[direita]
            lista[direita] = tmp

    tmp = lista[primeiro]
    lista[primeiro] = lista[direita]
    lista[direita] = tmp

    return direita

N = int(input())
iras = []
for _ in range(N):
    x = float(input())
    iras.append(x)

quick_sort(iras)

for x in iras[::-1]:
    print(f'{x:.2f}')
