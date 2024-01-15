print("Bienvenido al minijuego de preguntas")
jugar = input("¿Te gustaría jugar? ")
if jugar.lower() != "si":
    quit()

print("¡Empecemos!")

quest_point = 0

try:
    question_1 = int(input("¿Cuántos satélites tiene la luna? a) 1, b) 2, c) 0: "))
    if question_1 == 0:
        quest_point += 1
    question_2 = int(input("¿Cuántos planetas hay en nuestro sistema solar? a) 8, b) 12, c) 10: "))
    if question_2 == 8:
        quest_point += 1
    question_3 = input("¿La Tierra es el planeta más cercano al sol? a) Sí, b) Mercurio, c) Marte: ").lower()
    if question_3 == "marte":
        quest_point += 1
    question_4 = input("¿El satélite de la Tierra se llama Luna? a) Sí, b) Es Fobos, c) Es Calisto: ").lower()
    if question_4 == "si":
        quest_point += 1
    question_5 = int(input("¿Cuál es el porcentaje del nivel de superficie del mar en la Tierra? a) 80%, b) 54%, c) 70%: "))
    if question_5 == 70:
        quest_point += 1
    
    if quest_point < 3:
        print(f"Necesitas repasar un poco más, tu puntuación es {quest_point}")
    elif quest_point == 5:
        print(f"Puntuación perfecta! ¡Felicidades, tu puntuación es {quest_point}!")
    else:
        print(f"Tu puntuación es {quest_point}. ¡Bien hecho!")

except ValueError:
    print("Ingrese un valor numérico para su respuesta.")
