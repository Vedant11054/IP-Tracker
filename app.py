from flask import Flask, render_template, request, jsonify
import requests

app = Flask(_name_)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/lookup', methods=['POST'])
def lookup():
    mobile_number = request.form['mobile_number']
    api_url = f'https://api.numlookupapi.com/v1/validate/{mobile_number}?apikey=num_live_BdEsxjw0Wp5W4hAhEJF4bY3L756HIQD6rOPY1JBt'

    try:
        response = requests.get(api_url)
        data = response.json()

        if response.status_code == 200:
            is_valid = data.get('valid', False)
            if is_valid:
                number = data.get('number')
                country_code = data.get('country_code')
                country_name = data.get('country_name')
                location = data.get('location', 'Unknown')
                line_type = data.get('line_type', 'Unknown')

                return render_template('result.html', 
                                       message=f"Mobile number {number} is valid.",
                                       country=f"Country: {country_name} ({country_code})",
                                       location=f"Location: {location}",
                                       line_type=f"Line Type: {line_type}")
            else:
                return render_template('result.html', message=f"Mobile number {mobile_number} is invalid.")
        else:
            return render_template('result.html', message='Error validating mobile number.')
    
    except Exception as e:
        return render_template('result.html', message='Error validating mobile number.')

if _name_ == '_main_':
    app.run(debug=True)
