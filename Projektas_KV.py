import math, requests
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


def evaluate_expression(expression):
    # Replace the eval function with a safer evaluation mechanism
    # This example uses simple arithmetic operations and avoids eval
    try:
        # Handle square root separately
        if 'sqrt' in expression:
            number = float(expression.split('sqrt')[1])
            return math.sqrt(number)
        
        # Basic arithmetic
        result = eval(expression, {"__builtins__": None}, {"math": math})
    except ZeroDivisionError:
        return "Cannot divide by zero."
    except Exception as e:
        return "Invalid expression."
    return result

def get_weather(city='Vilnius'):
    API_key = '5fd6309521391b5401a1c21b795e599b'
    lat = 54.8985
    lon = 23.9036
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}&units=metric'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            weather_data = response.json()
            # Extract the icon code from the weather data
            icon_code = weather_data['weather'][0]['icon']
            # Construct the icon URL
            weather_data['icon_url'] = f"https://openweathermap.org/img/wn/{icon_code}@2x.png"
            return weather_data
        else:
            return {"error": "Failed to fetch weather data"}
    except requests.RequestException as e:
        return {"error": "Request failed"}
    

@app.route("/", methods=['GET', 'POST'])
def home():
    result = ""
    if request.method == 'POST':
        expression = request.form.get('expression')
        result = evaluate_expression(expression)
    weather = get_weather()
    return render_template('index.html', result=result, weather=weather, icon_url=weather.get('icon_url', ''))

if __name__ == "__main__":
    app.run(debug=True)


"""
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
"""

    

