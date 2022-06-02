'''
def exibe(v, n):
    i = 0
    while i < n:
        print(v[1], end='')
        i += 1
    print('\n')
    return exibe

def troca(v, i, j):
    temp = v[i]
    v[i] = v[j]
    v[j] = temp
    return troca

def empurra(v, n):
    i = 0
    while i < n-1:
        if v[i] > v[i+1]:
            troca(v, i, i+1)
        i +=1
    return empurra


def bubble_sort(v, n):
    exibe(v, n)
    tam = n
    while tam > 1:
        empurra(v, tam)
        exibe(v, tam)
        tam -=1
    else:
        exibe(v, n)
    return bubble_sort


bubble_sort([40,20,50,30,10], 5)
'''

def exibe(v, n):
    i = 0
    while i < n:
        print(v[i], end='')
        i += 1
    print('\n')
    return

def troca(v, i, j):
    temp = v[i]
    v[i] = v[j]
    v[j] = temp
    return


def empurrar(v, n):
    i = 0
    while i < n - 1:
        while v[i] > v[i + 1]:
            troca(v, i, i + 1)
        else:
            i += 1
    return


def bubble_sort(v, n):
    exibe(v, n)
    tam = n
    while tam > 1:
        empurrar(v, tam)
        exibe(v, tam)
        tam -= 1
    exibe(v, n)
    return

bubble_sort([40,20,50,30,10], 5)
