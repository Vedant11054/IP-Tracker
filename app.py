from flask import Flask, request, render_template, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/track-ip', methods=['POST'])
def track_ip():
    ip_address = request.form['ip']
    access_token = 'your_token_here'
    url = f'https://ipinfo.io/{ip_address}?token={access_token}'
    response = requests.get(url)
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": "Failed to retrieve information"}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)
