from flask import Flask, render_template, request, jsonify

# Configureer Flask om de hoofdmap als static en templates folder te gebruiken
app = Flask(__name__, template_folder='.', static_folder='.')

log_file = "log.txt"  # Bestandsnaam voor logging

# Route om de HTML-pagina te laden
@app.route('/')
def index():
    email = request.args.get('email')  # Optioneel: krijg e-mailadres uit querystring
    if email:
        with open(log_file, 'a') as file:
            file.write(f"Email geopend: {email}\n")
    return render_template('index.html')

# Route om naam te verwerken
@app.route('/submit-name', methods=['POST'])
def submit_name():
    name = request.form.get('name')
    with open(log_file, 'a') as file:
        file.write(f"Naam ingevuld: {name}\n")
    return jsonify({"status": "ok"})

# Route om locatie toestemming te loggen
@app.route('/log-location', methods=['POST'])
def log_location():
    latitude = request.form.get('latitude')
    longitude = request.form.get('longitude')
    with open(log_file, 'a') as file:
        file.write(f"Locatie toestemming gegeven: {latitude}, {longitude}\n")
    return jsonify({"status": "ok"})

# Route om e-mail te loggen
@app.route('/submit-email', methods=['POST'])
def submit_email():
    email = request.form.get('email')
    with open(log_file, 'a') as file:
        file.write(f"E-mail ingevuld: {email}\n")
    return jsonify({"status": "ok"})

if __name__ == '__main__':
    app.run(debug=True)
