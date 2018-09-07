import random
import time
import os
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

        
def geraNumerosAleatorios(vetor, tamanho):
    vetor = random.sample(range(1000000),  tamanho)
    # print(vetor)
    return vetor
    
def heapify(vetor, n, i):
    maior = i 
    esquerda = 2 * i + 1     
    direita = 2 * i + 2     

    if esquerda < n and vetor[i] < vetor[esquerda]:
        maior = esquerda

    if direita < n and vetor[maior] < vetor[direita]:
        maior = direita
 
    if maior != i:
        vetor[i],vetor[maior] = vetor[maior],vetor[i] 
        heapify(vetor, n, maior)
 
def heapSort(vetor):
    n = len(vetor)

    for i in range(n, -1, -1):
        heapify(vetor, n, i)
 
    for i in range(n-1, 0, -1):
        vetor[i], vetor[0] = vetor[0], vetor[i] 
        heapify(vetor, i, 0)
 
def swap(vetor, n, m):
    aux = vetor[n]
    vetor[n] = vetor[m]
    vetor[m] = aux

def particiona(vetor, posInicial, posFinal):
    pivot = vetor[posInicial] #Pivô da extrema esquerda (Lomuto)
    i = posInicial #Posição final do pivô
    j = posInicial + 1 #percorre o resto do vetor

    while j <= posFinal:
        if vetor[j] < pivot:
            i += 1 #achou elemento > o pivô
            swap(vetor, i, j)
        j += 1 
    swap(vetor, posInicial, i)
    return i

def quicksort(vetor, posInicial, posFinal):
    if posInicial < posFinal: #passo recursivo para ordenar vetores com mais de 2 elementos
        pivot = particiona(vetor, posInicial, posFinal)
        quicksort(vetor, posInicial, pivot - 1) #Recursividade para ordenar à esquerda (números menores que o pivô)
        quicksort(vetor, pivot+1, posFinal) #Recursividade para ordenar à direita (números maiores que o pivô)

def merge(vetor, posInicial, pivotMeio, posFinal):
    aux = vetor.copy() 
    i = posInicial #Inicio do subvetor da esquerda
    j = pivotMeio + 1 #Inicio do subvetor da direita
    k = posInicial #Inicio vetor grande

    while k <= posFinal: 
        if i > pivotMeio: #Quando não tiver mais elementos no subvetor da esquerda
            vetor[k] = aux[j] 
            j += 1
        elif j > posFinal: #Quando não tiver mais elementos no subvetor da direita
            vetor[k] = aux[i] 
            i += 1
        elif aux[i] <= aux[j]: #Compara se o elemento do subvetor da esquerda é <= o da direita
            vetor[k] = aux[i] 
            i += 1
        else: #Nesse caso, deve-se retirar o elemento do subvetor da direita
            vetor[k] = aux[j]
            j += 1
        k += 1

def mergesort(vetor, posInicial, posFinal):
    if posInicial < posFinal:
        pivotMeio = (posFinal + posInicial) // 2 #Meio do vetor
        mergesort(vetor, posInicial, pivotMeio) #Subvetor da esquerda do centro do vetor
        mergesort(vetor, pivotMeio + 1, posFinal) #Subvetor da direita do centro do vetor
        merge(vetor, posInicial, pivotMeio, posFinal)

def shellsort(vetor):
    h = len(vetor) // 2 #Metade do vetor
 
    while h > 0:
        i = h
        while i < len(vetor):
            aux = vetor[i]
            troca = False
            j = i - h
            while j >= 0 and vetor[j] > aux:
                vetor[j+h] = vetor[j]
                troca = True
                j -= h
            if troca:
                vetor[j+h] = aux
            i += 1
        h = h // 2

os.system('clear')
vetor = []
vetorHeapSort = []
vetorQuickSort = []
vetorMergeSort = []
vetorShellSort = []

tamanho = int(input("Tamanho do vetor: "))
vetor = geraNumerosAleatorios(vetor, tamanho)
os.system('clear')
# print('Vetor Original: ')
# print(vetor)

vetorHeapSort = vetor.copy()
vetorQuickSort = vetor.copy()
vetorMergeSort = vetor.copy()
vetorShellSort = vetor.copy()

tempoAntesHeap = time.time()
heapSort(vetorHeapSort)
tempoDepoisHeap = time.time()
tempoHeap = (tempoDepoisHeap - tempoAntesHeap) * 1000
print('Vetor Ordenado por Heap Sort: ')
# print(vetorHeapSort)
print('O tempo de execucao do Heap Sort foi de: %0.2f ms' %tempoHeap)
print('\n')

# print('Vetor Original: ')
# print(vetorQuickSort)
tempoAntesQuick = time.time()
quicksort(vetorQuickSort, 0, len(vetorQuickSort)-1)
tempoDepoisQuick = time.time()
tempoQuick = (tempoDepoisQuick - tempoAntesQuick) * 1000
print('Vetor ordenado por Quick Sort: ')
# print(vetorQuickSort)
print('O tempo de execucao do Quick Sort foi de: %0.2f ms' %tempoQuick)
print('\n')

# print('Vetor Original: ')
# print(vetorMergeSort)
tempoAntesMerge = time.time()
mergesort(vetorMergeSort, 0, len(vetorMergeSort)-1)
tempoDepoisMerge = time.time()
tempoMerge = (tempoDepoisMerge - tempoAntesMerge) * 1000
print('Vetor ordenado por Merge Sort: ')
# print(vetorMergeSort)
print('O tempo de execucao do Merge Sort foi de: %0.2f ms' %tempoMerge)
print('\n')

# print('Vetor Original: ')
# print(vetorShellSort)
tempoAntesShell = time.time()
shellsort(vetorShellSort)
tempoDepoisShell = time.time()
tempoShell = (tempoDepoisShell - tempoAntesShell) * 1000
print('Vetor ordenado por Shell Sort: ')
# print(vetorShellSort)
print('O tempo de execucao do Shell Sort foi de: %0.2f ms' %tempoShell)
print('\n')

y = tempoHeap*np.array(range(len(vetorHeapSort))) / tamanho
y2 = tempoQuick*np.array(range(len(vetorQuickSort))) / tamanho
y3 = tempoMerge*np.array(range(len(vetorMergeSort))) / tamanho
y4 = tempoShell*np.array(range(len(vetorShellSort))) / tamanho

plt.plot(vetorHeapSort, y)
plt.plot (vetorQuickSort,y2, color='red')
plt.plot (vetorMergeSort, y3, color='green')
plt.plot (vetorShellSort, y4, color='purple')
plt.title("Algoritmos nLog(n)")
red_patch = mpatches.Patch(color='red', label='Quick Sort')
blue_patch = mpatches.Patch(color='blue', label='Heap Sort')
green_patch = mpatches.Patch(color='green', label='Merge Sort')
purple_patch = mpatches.Patch(color='purple', label='Shell Sort')
plt.legend(handles=[red_patch, blue_patch, green_patch, purple_patch])

plt.show()


