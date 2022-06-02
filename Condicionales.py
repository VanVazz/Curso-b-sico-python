#declaramos una variable
calificación = input("introduce tu calificación de la AZ-900:")
calificación = int(calificación)
#preguntamos si la calificación es menor a 700
if calificación < 700 :
     print("vesss, por no estudiar") #si es menor a 700, muestra esto
elif calificación > 1000 :
    print("Mientes!!!! No puedes sacar más de 1000")
else : #si no se cumple el if anterior, pasa a esta línea
    print("felicidades pasa por tu certificado") #se ejecuta si ninguno de los of cumple
#Verificador de mayoría de edad
edad = input("Introduce tu edad: ")
edad = int(edad)

if edad >= 18 and edad <= 100 :
    print("Bienvenido al mamitas. Pase a la perdición")
elif edad > 100 :
    print("Si vienes acompañado de tus abuelitos, si te podemos fiar")
elif edad < 0 :
    print("ni que fueras viajer@ del tiempo")
else : #NO OLVIDAR LOS :
    print("no puedes llevarte esos cigarros")

    #en python no hay SWITCH CASE