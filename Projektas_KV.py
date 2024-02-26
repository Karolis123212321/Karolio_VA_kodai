import math
from flask import Flask, request

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

@app.route("/") 
def hello_world():

    return f"""
                <form action="/skaicius">
                    <label for="test">skaicius 1</label><br>
                        <input type="text" id="test" name="test" value="0"><br>
                        </br></br>

                    <label for="test2">skaicius 2</label><br>
                        <input type="text" id="test2" name="test2" value="0"><br><br>
                        </br></br>
                        
                    <label for="[[__ID__]]">skaicius 2</label><br>   
                        <input type="text" id="[[__ID__]]" name="[[__ID__]]" value="0"><br><br>
                        </br></br>

                    <input type="submit" value="Submit">
             """   
@app.route("/skaiciuokle")
def skaiciuokle():
    skaicius1 = request.args.get("sk1")
    skaicius2 = request.args.get("sk2")
    suma = prideti(int(skaicius1), int(skaicius2))
    return f"{suma}"

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


    

