from random import randint
path_preguntas = "./Preguntas.txt"
Preguntas = open(path_preguntas,"r")
path_respuestas = "./Respuestas.txt"
Respuestas = open(path_respuestas,"r")
Lista_Preguntas = Preguntas.readlines()
Lista_Respuestas = Respuestas.readlines()
Respuestas.close()
Preguntas.close()
tope = len(Lista_Preguntas)
if tope != len(Lista_Respuestas):
    raise NameError("La cantidad de preguntas no es la misma cantidad de respuestas \n")
total_preguntas = 0
preguntas_correctas = 0
while(True):
    numero_de_pregunta = randint(0,tope - 1)
    numero_de_respuesta = numero_de_pregunta
    print(Lista_Preguntas[numero_de_pregunta][:-1], end = " ")
    try:
        respuesta = int(input())
    except ValueError:
        print("\nGracias por jugar este juego")
        print("%d / %d de aciertos"%(preguntas_correctas,total_preguntas))
        input("Presione ENTER para salir: ")
        break
    if(respuesta == int(Lista_Respuestas[numero_de_respuesta].strip())):
        print("Correcto\n")
        preguntas_correctas += 1
        total_preguntas += 1
    elif(respuesta != ""):
        print("   Incorrecta. Respuesta: " + Lista_Respuestas[numero_de_respuesta])
        total_preguntas += 1
    else:
        break
