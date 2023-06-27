from lista import *
archivosalida = open ("salida.txt", 'w')
with open("codigo_ejemplo.txt") as archivo:
     

     for linea in archivo:
          palabras = linea.split(' ')
          print (palabras)
          findelinea = 0
          cont = 0
          while (findelinea==0):
               
               valida = automata_inicio (palabras[cont])
               if(valida[0]==1):
                    print ("valida", valida)
                    print(valida [1])
                    with open ("salida.txt", 'a') as archivosalida:
                         archivosalida.write(valida[1]+" ")
                    if(valida [2]==1):
                        findelinea = 1
                        break;
                    else:
                         cont=cont+1
                         
               valida = automata_puntoycoma (palabras[cont])
               if(valida[0]):
                    print(valida [1])
                    with open ("salida.txt", 'a') as archivosalida:
                         archivosalida.write(valida[1]+"\n")
                    if(valida [2]):
                        findelinea = 1
                        break;
                    else:
                         cont=cont+1

               valida = automata_escribe (palabras[cont])
               print ("valida", valida)
               if(valida[0]==1):
                    print(valida [1])
                    with open ("salida.txt", 'a') as archivosalida:
                         archivosalida.write(valida[1]+" ")
                    if(valida [2]==1):
                        findelinea = 1
                        break;
                    else:
                         cont=cont+1

               valida = automata_cadena (palabras[cont])
               if(valida[0]==1):
                    print ("valida", valida)
                    print(valida [1])
                    with open ("salida.txt", "a") as archivosalida:
                         archivosalida.write(valida[1]+" ")
                    if(valida [2]==1):
                        findelinea = 1
                        break;
                    else:
                         cont=cont+1

               valida = automata_puntoycoma (palabras[cont])
               if(valida[0]):
                    print(valida [1])
                    with open ("salida.txt", 'a') as archivosalida:
                         archivosalida.write(valida[1]+"\n")
                    if(valida [2]):
                        findelinea = 1
                        break;
                    else:
                         cont=cont+1

                                   
               valida = automata_fin (palabras[cont])
               if(valida[0]==1):
                    print ("valida", valida)
                    print(valida [1])
                    with open ("salida.txt", 'a') as archivosalida:
                         archivosalida.write(valida[1]+" ")
                    if(valida [2]==1):
                        findelinea = 1
                        break;
                    else:
                         cont=cont+1

               valida = automata_puntoycoma (palabras[cont])
               if(valida[0]):
                    print(valida [1])
                    with open ("salida.txt", 'a') as archivosalida:
                         archivosalida.write(valida[1]+" ")
                    if(valida [2]):
                        findelinea = 1
                        break;
                    else:
                         cont=cont+1
                         
               archivosalida.write ("\n")
               with open ("salida.txt", 'a') as archivosalida:
                    archivosalida.write(valida[1])
