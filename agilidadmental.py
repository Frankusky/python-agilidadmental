"""
Juego inspirado en la aplicacion "Agilidad mental" para Android.
Adaptado en python por Frank Sam Hu
V 1.3 Arreglado error de pistas, agregado ciclo while para salir
"""
import random
import time

#**************************Subprogramas*****************************
def numazar():
    numeros = ['1', '2', '3', '4', '5', '6']
    cont = 0
    numero = ""
    while (cont<=3):
        digito = random.choice(numeros)
        numeros.remove(digito)
        numero = numero + str(digito)
        cont = cont+1
    return numero

def comprobador(numusu): 
    x = 0
    valido = True
    while (x!=4):
    #Comprobar que no se ingrese numeros mayores que 7 o menores que 0
        if (int(numusu[x])>=7 or int(numusu[x])<=0) or numusu[0]=="-":
            valido = False
        x = x+1
    #Comprobar que no se repitan los numeros
    if (numusu[0]==numusu[1] or numusu[0]==numusu[2] or numusu[0]==numusu[3] or numusu[1]==numusu[2] or numusu[1]==numusu[3] or numusu[2]==numusu[3]):
        valido = False
    return valido

def numcor(numusu,adivinar):
    #pistas si el numero esta en su posicion correcta
    x=0
    contfijo = 0
    while (x<=3):
        if(numusu[x]==adivinar[x]):
            contfijo = contfijo + 1
        x = x+1
    return contfijo

def numcer(numusu,adivinar):
    #pistas si el numero esta presente pero no en su posicion
    contcer = 0
    x = 0
    y = 0
    while (x<=3 and y<=3):
        while (y<=3):
            if (x==y and y!=3):
                y+=1
            if (numusu[x]==adivinar[y]):
                contcer+=1
                if (x==3 and y==3):
                    contcer-=1
            y+=1
        x+=1
        y=0
    return contcer
#***************************Programa principal************************
#Creando numero al azar
print " ______  _                             _     _            "
print "(____  \(_)                           (_)   | |           "
print " ____)  )_  ____ ____ _   _ ____ ____  _  _ | | ___   ___ "
print "|  __  (| |/ _  )  _ \ | | / _  )  _ \| |/ || |/ _ \ /___)"
print "| |__)  ) ( (/ /| | | \ V ( (/ /| | | | ( (_| | |_| |___ |"
print "|______/|_|\____)_| |_|\_/ \____)_| |_|_|\____|\___/(___/ "
print "\t\t\tV1.3\n\t\t\tBy: Frank Sam Hu\n\n"
print "*-"*15+"* Instrucciones *"+"-*"*15
print "Las reglas de este juego son simples:"
print """1. Debes encontrar un numero de 4 digitos.
2. Solo se admiten numeros del 1 al 6.
3. Los numeros no se repiten.
4. Solamente tienes 10 vidas.
5. Si adivinas un numero y esta en su posicion, aparecera un *.
6. Si adivinas un numero pero no esta en su posicion, aparecera un #.
7. La posicion en que aparezcan los # y * no indican el lugar donde acertaste tu numero.
"""
print "*-"*38,"*"
resp = "si"
while (resp == "si"):
    adivinar = numazar()
    #print adivinar
    vidas = 10
    terminado = False
    while(terminado != True):
    #Comprobar si lo ingresado sea un numero de 4 digitos
        ing_aprob = False
        while(ing_aprob == False):
            numusu = raw_input("Ingrese un numero de 4 digitos: ")
            if(len(numusu)!=4 or numusu.isdigit() == False):
                print "Lo que haz ingresado no es valido!"
            else: 
                while (comprobador(numusu)==False):
                    print "Error! Haz hecho algo mal, lee bien las instrucciones!"
                    numusu = raw_input("Vuelve a intentarlo:")
                    comprobador(numusu)
                ing_aprob = True
        #revisando si gano o no
        if(numusu == adivinar):
            print "Felicidades! Ganaste!!!"
            terminado = True
            time.sleep(3)
        else:
            vidas = vidas - 1
            if (vidas == 0):
                terminado = True
                print "Oww! Mala suerte :( Te haz quedado sin vidas"
                print "El numero que tenias que adivinar era: ", adivinar
                print "Xx"*10+"X --  G  A  M  E  --  O V E R  -- X"+"xX"*10
                time.sleep(3)
            else:
                print "Fallaste! te quedan ", vidas, " vidas!"
                print "*"*numcor(numusu,adivinar)
                print "#"*numcer(numusu,adivinar)
                print ""
    resp = (raw_input("Desea volver a jugar? (Si o no): ")).lower()
            
