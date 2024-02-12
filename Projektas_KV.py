import math
def prideti (pirmas, antras):
    return pirmas + antras

def atimti (pirmas, antras):
    return pirmas + antras

def dauginti (pirmas, antras):
    return pirmas + antras

def dalinti (pirmas, antras):
    return pirmas + antras

pasirinkimas = input("Ka darysite? +|-|*|/")
numeris_1 = int(input("Iveskite x"))
numeris_2 = int(input("Iveskite y"))

if pasirinkimas == '+':
    print("Atsakymas: ", prideti(numeris_1, numeris_2))
    
elif pasirinkimas == '-':
    print("Atsakymas: ", atimti(numeris_1, numeris_2))
    
elif pasirinkimas == '*':
    print ("Atsakymas: ", dauginti(numeris_1, numeris_2))
    
elif pasirinkimas == '/':
    print("Atsakymas: ", dalinti(numeris_1, numeris_2))
    



