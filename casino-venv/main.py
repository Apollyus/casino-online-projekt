from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        # Získání dat z formuláře
        name = request.form['name']
        age = request.form['age']

        # Zpracování dat (zde jen jednoduchý výstup)
        response = {'message': f'Hello {name}, you are {age} years old!'}
        return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
