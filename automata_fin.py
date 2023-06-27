def automata_fin(cadenaEjemplo):
  token = 'N'
  findelinea = 0
  Q= [0,1,2,3,4,5]
  sigma = ['f',"i","n",';',' ']
  q0= 0
  F=[4,5]
  delta = {
      'f':[1,'E','E','E','E'],
      'i':['E',2,'E','E','E'],
      'n':['E','E',3,'E','E'],
      ';':['E','E','E',4,'E'],
      ' ':['E','E','E','E',5]
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
    token = "NAV"
  else:
    validad = 0

  if (estadoActual == 4):
    findelinea = 0
  elif (estadoActual == 5):
    findelinea = 1

  return [validad,token,findelinea]

##entrada = input("Ingresa cadena a evaluar: ")
##salida=automata_fin(entrada)
##print(salida)
