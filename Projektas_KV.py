import math
from flask import Flask, request, render_template

app = Flask(__name__)


def prideti (pirmas, antras):
    return pirmas + antras

def atimti (pirmas, antras):
    return pirmas - antras

def dauginti (pirmas, antras):
    return pirmas * antras

def dalinti (pirmas, antras):
    return pirmas / antras

def saknis (pirmas):
    return math.sqrt(pirmas)

buve_veiksmai = []

@app.route("/") 
def inputas():
    return render_template('index.html')

@app.route("/skaiciuokle")
def skaiciuokle():
    global buve_veiksmai
    skaicius1 = int(request.args.get("sk1"))
    veiksmas = request.args.get("zenklas")
    if veiksmas == "sqrt":
        if skaicius1 < 0:
            rezultatas = "Negalima traukti šaknies iš nulio"
        else:
            rezultatas = saknis(skaicius1)
    else:
        
        skaicius2 = int(request.args.get("sk2"))
        if veiksmas == "+":
            rezultatas = prideti(skaicius1,skaicius2)
        
        elif veiksmas == "-":
            rezultatas = atimti(skaicius1, skaicius2)

        elif veiksmas == "/":
            rezultatas = dalinti(skaicius1, skaicius2)

        elif veiksmas == "*":
            rezultatas = dauginti(skaicius1, skaicius2)

        elif veiksmas == "sqrt":
            rezultatas = saknis(skaicius1)
    if veiksmas == "sqrt":
        buve_veiksmai.append(f"{veiksmas} iš {skaicius1} = {rezultatas}")
    else:
        buve_veiksmai.append(f"{skaicius1} {veiksmas} {skaicius2} = {rezultatas}")

    return render_template('index.html', ats = rezultatas, veiksmai = buve_veiksmai)


if __name__ == "__main__":
    app.run()




while True:
    print ("Pasirinkite skaiciuotuvo versija:")
    print ("n - naturalus")
    print ("p - Su paaiskinimais")

    Versija = input("Pasirinkimas: ")


    if Versija == 'n':
        while True:
            tekstas = str(input())
            a, b, c = tekstas.split(' ')
            a = int(a)
            c = int(c)
            if b == '+':
                print("Atsakymas: ",a + c)
                break
            elif b == '-':
                print("Atsakymas: ",a - c)
                break
            elif b == '*':
                print("Atsakymas: ",a * c)
                break
            elif b == '/':
                print("Atsakymas: ",a / c)
                break

    elif Versija == 'p':
        while True:
            print ("Pasirinkite kokia operacija norite daryti:")
            print ("1 - sudetis")
            print ("2 - atimtis:")
            print ("3 - daugyba:")
            print ("4 - dalyba:")
            print ("5 - saknies istraukimas")
            print ("6 - pabaigti darba")

            pasirinkimas = input("Pasirinkimas: ")
            if pasirinkimas == '5':
                skaicius = int(input("Iveskite skaiciu: "))
                print ("Atsakymas: ", saknis(skaicius))
                continue
            if pasirinkimas == '6':
                break
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


    

