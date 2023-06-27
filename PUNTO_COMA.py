import sys

# inicializar variables


def automata_puntoycoma(cadenaEjemplo):
    token = 'T'
    findelinea = 0
    Q = [0, 1]
    sigma = [';']
    q0 = 0
    F = [1]
    delta = {
        ';': [1, 'E']
    }
    # cadenaEjemplo = 'baaa'
    logitudCadena = len(cadenaEjemplo)

    estadoActual = q0
    for cabezalDeLectura in range(0, logitudCadena):
        simboloEvaluado = str(cadenaEjemplo[cabezalDeLectura])
        if simboloEvaluado in sigma:
            estadoActual = delta[simboloEvaluado][estadoActual]
            print(estadoActual, simboloEvaluado)
            if (estadoActual) == 'E':
                break
            # cabezalDeLectura = cabezalDeLectura+1
        else:
            break

    if (estadoActual in F):
        validad = 1
        token = "TES"
        findelinea = 1
    else:
        validad = 0
        findelinea = 0


    return [validad, token, findelinea]


def main(codigo_ejemplo):
    with open(codigo_ejemplo[1]) as archivo:
        for linea in archivo:
            palabras = linea.split(' ')
            findelinea = 1
            cont = 0
            while (findelinea):
                valida = automata_inicio(palabras[cont])
                print(valida)
                findelinea = 0


##if __name__ == "__main__":
##    main(sys.codigo_ejemplo)
