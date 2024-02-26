import math
from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculate():
    if request.method == "POST":
        operation = request.form.get("operation")
        if operation == "saknis":
            number = float(request.form.get("number"))
            result = math.sqrt(number)
            return render_template_string(HTML_TEMPLATE, result=int(result))
        else:
            number1 = float(request.form.get("number1"))
            number2 = float(request.form.get("number2"))
            if operation == "sudetis":
                result = number1 + number2
            elif operation == "atimtis":
                result = number1 - number2
            elif operation == "daugyba":
                result = number1 * number2
            elif operation == "dalyba":
                result = number1 / number2
            return render_template_string(HTML_TEMPLATE, result=result)
    else:
        return render_template_string(HTML_TEMPLATE)

HTML_TEMPLATE = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Kalkuliatorius 1.0</title>
</head>
<body>
  <h2>Kalkuliatorius 1.0</h2>
  <form method="post">
    <label for="operation">Pasirinkite ka darysite</label>
    <select name="operation" id="operation">
      <option value="sudetis">sudetis</option>
      <option value="atimtis">Atimtis</option>
      <option value="daugyba">Daugyba</option>
      <option value="dalyba">Dalyba</option>
      <option value="saknis">Saknis</option>
    </select>
    <br><br>
    <input type="number" id="number1" name="number1" placeholder="1 numeris" required>
    <input type="number" id="number2" name="number2" placeholder="2 numeris">
    <input type="number" id="number" name="number" placeholder="Numeris sakniai">
    <button type="submit">Skaiciuoti</button>
  </form>
  {% if result is defined %}
  <h3>Atsakymas: {{ result }}</h3>
  {% endif %}
</body>
</html>
"""

if __name__ == "__main__":
    app.run(debug = True)


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


    

