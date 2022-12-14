'''
Proyecto final

Fernando Daniel Castillo Barrón - 418002784
Ramón Cruz Perez - 315008148
Marta Yunnuen Pacheco - 
Oscar Emilio Caballero Jimenez - 

'''

def leerFASTA(pathArchivo):
    archivo = open(pathArchivo, "r")
    cabereza = archivo.readline()
    adn = archivo.readline()
    return adn


# Función para encontrar la subcadena común más larga de las secuencias `X[0…m-1]` e `Y[0…n-1]`
# Obtenido de: https://www.techiedelight.com/es/longest-common-substring-problem/
def LCS(X, Y):
    m = len(X)
    n = len(Y)
 
    maxLength = 0           # almacena la longitud máxima de LCS
    endingIndex = m         # almacena el índice final de LCS en `X`
 
    # `lookup[i][j]` almacena la longitud de LCS de la subcadena `X[0…i-1]` e `Y[0…j-1]`
    lookup = [[0 for x in range(n + 1)] for y in range(m + 1)]
 
    # llenar la tabla de búsqueda de forma ascendente
    for i in range(1, m + 1):
        for j in range(1, n + 1):
 
            # si el carácter actual de `X` e `Y` coincide
            if X[i - 1] == Y[j - 1]:
                lookup[i][j] = lookup[i - 1][j - 1] + 1
 
                # actualiza la longitud máxima y el índice final
                if lookup[i][j] > maxLength:
                    maxLength = lookup[i][j]
                    endingIndex = i
 
    # devuelve la subcadena común más larga que tiene una longitud `maxLength`
    return X[endingIndex - maxLength: endingIndex]

humanh11 = leerFASTA('./humanh11.txt')
humanh12 = leerFASTA('./humanh12.txt')
macaca11 = leerFASTA('./macacah11.txt')
macaca12 = leerFASTA('./macacah12.txt')

print('--- GENES PARALOGOS ---')
print('')
print('Human histone h1.1: ', humanh11)
print('Human histone h1.2: ', humanh12)
print('Cadena común más larga: ', LCS(humanh11, humanh12))
print('')
print('Macaca fascicularis histone h1.1: ', macaca11)
print('Macaca fascicularis histone h1.2: ', macaca12)
print('Cadena común más larga: ', LCS(macaca11, macaca12))
print('')
print('--- GENES ORTOLOGOS ---')
print('')
print('Human histone h1.1: ', humanh11)
print('Macaca fascicularis histone h1.1: ', macaca11)
print('Cadena común más larga: ', LCS(humanh11, macaca11))
print('')
print('Human histone h1.2: ', humanh12)
print('Macaca fascicularis histone h1.2: ', macaca12)
print('Cadena común más larga: ', LCS(humanh12, macaca12))
print('')