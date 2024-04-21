from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def get_ip_info(ip_address):
    url = f"https://ipinfo.io/{ip_address}/json"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            city = data.get('city', 'Unknown')
            region = data.get('region', 'Unknown')
            country = data.get('country', 'Unknown')
            isp = data.get('org', 'Unknown')
            return {
                'City': city,
                'Region': region,
                'Country': country,
                'ISP': isp
            }
        else:
            return None
    except requests.exceptions.RequestException:
        return None

@app.route('/', methods=['GET', 'POST'])
def home():
    ip_info = None
    if request.method == 'POST':
        ip_address = request.form['ip_address']
        if ip_address:
            ip_info = get_ip_info(ip_address)
    return render_template('index.html', ip_info=ip_info)

if __name__ == '__main__':
    app.run(debug=True)
