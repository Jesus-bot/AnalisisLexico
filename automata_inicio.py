def automata_inicio(cadenaEjemplo):
  token = 'N'
  findelinea = 0
  Q= [0,1,2,3,4,5,6,7,8]
  sigma = ['i','n','c','o',';',' ']
  q0= 0
  F=[7,8]
  delta = {
      'i':[1,'E',3,'E',5,'E','E','E'],
      'n':['E',2,'E','E','E','E','E','E'],
      'c':['E','E','E',4,'E','E','E','E'],
      'o':['E','E','E','E','E',6,'E','E'],
      ';':['E','E','E','E','E','E',7,'E'],
      ' ':['E','E','E','E','E','E','E',8]
}
  logitudCadena = len(cadenaEjemplo)

  estadoActual = q0
  for cabezalDeLectura in range(0,logitudCadena):
    simboloEvaluado= str(cadenaEjemplo[cabezalDeLectura])
    if simboloEvaluado in sigma:
      estadoActual = delta[simboloEvaluado][estadoActual]
      print(estadoActual,simboloEvaluado)
      if(estadoActual)=='E':
        break
    else:
      break

  if (estadoActual in F):
    validad = 1
    token = "PR1"
  else:
    validad = 0

  if (estadoActual == 7):
    findelinea = 0
  elif (estadoActual == 8):
    findelinea = 1

  return [validad,token,findelinea]

##entrada = input("Ingresa cadena a evaluar: ")
##salida=automata_inicio(entrada)
##print("validad 1")
