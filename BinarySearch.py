# Algoritmo de busca binária
# Complexidade: O(log n)

lista1 = [1, 3, 5, 7, 9]

lista2 = [-12, 11, 45, 221, 319, 347]

def BinarySearch(array, searchableElement):

    maxIndex = len(array) - 1

    minIndex = 0

    while len(array) > 1:

        indexAttempt = (maxIndex + minIndex) // 2
        
        elementAttempt = array[indexAttempt]

        if elementAttempt == searchableElement:

            print(f'Elemento encontrado no índice {indexAttempt}')
            return indexAttempt
        
        if elementAttempt > searchableElement:

            maxIndex = indexAttempt - 1

        if elementAttempt < searchableElement:

            minIndex = indexAttempt + 1

    return None


BinarySearch(lista1, 9)