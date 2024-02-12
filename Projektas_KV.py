import math
def prideti (pirmas, antras):
    return pirmas + antras

def atimti (pirmas, antras):
    return pirmas - antras

def dauginti (pirmas, antras):
    return pirmas * antras

def dalinti (pirmas, antras):
    return pirmas / antras

print ("Pasirinkite kokia operacija norite daryti:")
print ("1 - sudetis")
print ("2 - atimtis:")
print ("3 - daugyba:")
print ("4 - dalyba:")

pasirinkimas = input("Pasirinkimas: ")
numeris_1 = int(input("Iveskite x: "))
numeris_2 = int(input("Iveskite y: "))

if pasirinkimas == '1':
    print("Atsakymas: ", prideti(numeris_1, numeris_2))
    
elif pasirinkimas == '2':
    print("Atsakymas: ", atimti(numeris_1, numeris_2))
    
elif pasirinkimas == '3':
    print ("Atsakymas: ", dauginti(numeris_1, numeris_2))
    
elif pasirinkimas == '4':
    print("Atsakymas: ", dalinti(numeris_1, numeris_2))
    



