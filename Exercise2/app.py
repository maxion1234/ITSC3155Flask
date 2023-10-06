from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/check', methods=['GET'])
def check_number():
    number = request.args.get('number')

    if number is None or number == "":
        result = "No input provided"
    else:
        try:
            number = int(number)
            if number % 2 == 0:
                result = f"{number} is even"
            else:
                result = f"{number} is odd"
        except ValueError:
            result = f"'{number}' is not a number"

    return render_template('check.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
