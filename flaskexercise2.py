from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/result', methods=['GET'])
def result():
    try:
        number = int(request.args.get('number'))
        if number % 2 == 0:
            message = f"{number} is an even number."
        else:
            message = f"{number} is an odd number."
    except ValueError:
        message = "Please enter a valid integer."

    return render_template('result.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)