def automata_escribe(cadenaEjemplo):
  token = 'N'
  findelinea = 0
  Q= [0,1,2,3,4,5,6,7,8,9]
  sigma = ['e','s','c','r','i','b',';',' ']
  q0= 0
  F=[8,9]
  delta = {
      'e':[1,'E','E','E','E','E',7,'E','E'],
      's':['E',2,'E','E','E','E','E','E','E'],
      'c':['E','E',3,'E','E','E','E','E','E'],
      'r':['E','E','E',4,'E','E','E','E','E'],
      'i':['E','E','E','E',5,'E','E','E','E'],
      'b':['E','E','E','E','E',6,'E','E','E'],
      ';':['E','E','E','E','E','E','E',8,'E'],
      ' ':['E','E','E','E','E','E','E','E',9]
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
    token = "BBS"
  else:
    validad = 0

  if (estadoActual == 8):
    findelinea = 0
  elif (estadoActual == 9):
    findelinea = 1

  return [validad,token,findelinea]

##entrada = input("Ingresa cadena a evaluar: ")
##salida=automata_escribe(entrada)
##print(salida)
