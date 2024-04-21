from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/track', methods=['POST'])
def track():
    ip_address = request.remote_addr
    with open('iplog.txt', 'a') as f:
        f.write(ip_address + '\n')
    return render_template('track.html', ip_address=ip_address)

if __name__ == '__main__':
    app.run(debug=True)
