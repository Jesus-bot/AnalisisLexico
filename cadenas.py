def automata_cadena(cadenaEjemplo):
    token = 'N'
    findelinea = 0
    Q = [0, 1, 2, 3, 4, 5]
    sigma = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
    'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
    'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','=', '"', '0','1', '2', '3', '4', '5', '6', '7', '8', '9']
    q0 = 0
    F = [5]
    delta = {
        'A': [1, 4, 4, 4, 4,'E'],
        'B': [4, 4, 4, 4, 4,'E'],
        'C': [4, 4, 4, 4, 4,'E'],
        'D': [4, 4, 4, 4, 4,'E'],
        'E': [4, 4, 4, 4, 4,'E'],
        'F': [4, 4, 4, 4, 4,'E'],
        'G': [4, 4, 4, 4, 4,'E'],
        'H': [4, 4, 4, 4, 4,'E'],
        'I': [4, 4, 4, 4, 4,'E'],
        'J': [4, 4, 4, 4, 4,'E'],
        'K': [4, 4, 4, 4, 4,'E'],
        'L': [4, 4, 4, 4, 4,'E'],
        'M': [4, 4, 4, 4, 4,'E'],
        'N': [4, 4, 4, 4, 4,'E'],
        'Ñ': [4, 4, 4, 4, 4,'E'],
        'O': [4, 4, 4, 4, 4,'E'],
        'P': [4, 4, 4, 4, 4,'E'],
        'Q': [1, 4, 4, 4, 4,'E'],
        'R': [4, 4, 4, 4, 4,'E'],
        'S': [4, 4, 4, 4, 4,'E'],
        'T': [4, 4, 4, 4, 4,'E'],
        'U': [4, 4, 4, 4, 4,'E'],
        'V': [4, 4, 4, 4, 4,'E'],
        'W': [4, 4, 4, 4, 4,'E'],
        'X': [4, 4, 4, 4, 4,'E'],
        'Y': [4, 4, 4, 4, 4,'E'],
        'Z': [4, 4, 4, 4, 4,'E'],
        'a': [1, 4, 4, 4, 4,'E'],
        'b': [4, 4, 4, 4, 4,'E'],
        'c': [4, 4, 4, 4, 4,'E'],
        'd': [4, 4, 4, 4, 4,'E'],
        'e': [4, 4, 4, 4, 4,'E'],
        'f': [4, 4, 4, 4, 4,'E'],
        'g': [4, 4, 4, 4, 4,'E'],
        'h': [4, 4, 4, 4, 4,'E'],
        'i': [4, 4, 4, 4, 4,'E'],
        'j': [4, 4, 4, 4, 4,'E'],
        'k': [4, 4, 4, 4, 4,'E'],
        'l': [4, 4, 4, 4, 4,'E'],
        'm': [4, 4, 4, 4, 4,'E'],
        'n': [4, 4, 4, 4, 4,'E'],
        'ñ': [4, 4, 4, 4, 4,'E'],
        'o': [4, 4, 4, 4, 4,'E'],
        'p': [4, 4, 4, 4, 4,'E'],
        'q': [1, 4, 4, 4, 4,'E'],
        'r': [4, 4, 4, 4, 4,'E'],
        's': [4, 4, 4, 4, 4,'E'],
        't': [4, 4, 4, 4, 4,'E'],
        'u': [4, 4, 4, 4, 4,'E'],
        'v': [4, 4, 4, 4, 4,'E'],
        'w': [4, 4, 4, 4, 4,'E'],
        'x': [4, 4, 4, 4, 4,'E'],
        'y': [4, 4, 4, 4, 4,'E'],
        'z': [4, 4, 4, 4, 4,'E'],
        '=': [2, 2, 'E', 'E', 'E', 'E'],
        '"': [3, 3, 3, 3, 5, 5],
        '0': ['E', 'E', 'E', 'E','E','E'],
        '1': ['E', 'E', 'E', 'E','E','E'],
        '2': ['E', 'E', 'E', 'E','E','E'],
        '3': ['E', 'E', 'E', 'E','E','E'],
        '4': ['E', 'E', 'E', 'E','E','E'],
        '5': ['E', 'E', 'E', 'E','E','E'],
        '6': ['E', 'E', 'E', 'E','E','E'],
        '7': ['E', 'E', 'E', 'E','E','E'],
        '8': ['E', 'E', 'E', 'E','E','E'],
        '9': ['E', 'E', 'E', 'E','E','E']

}
    logitudCadena = len(cadenaEjemplo)

    estadoActual = q0
    for cabezalDeLectura in range(0, logitudCadena):
      simboloEvaluado = str(cadenaEjemplo[cabezalDeLectura])
      if simboloEvaluado in sigma:
        estadoActual = delta[simboloEvaluado][estadoActual]
        print(estadoActual)
        if (estadoActual) == 'E':
          break
      else:
        break

    if (estadoActual in F):
      print("Es una cadena valida")
      validad = 1
      token = "SUN"
    else:
      validad = 0

    if (estadoActual == 5):
       findelinea = 0

    return [validad,token,findelinea]