from flask import Flask, render_template
import httpx

app = Flask(__name__)

services = [
    {
        'name': 'Kingsborough library website',
        'url': 'https://library.kbcc.cuny.edu/homepage',
        'status': None,
    },
    {
        'name': 'ILLiad',
        'url': 'https://kbcc-cuny.illiad.oclc.org/illiad/logon.html',
        'status': None,
    },
    {
        'name': 'dummy',
        'url': 'https://library.kbcc.cuny.edu/dummy',
        'status': None,
    }
]

@app.route('/')
def index():
    for service in services:
        try:
            response = httpx.get(service['url'])
            service['status'] = response.status_code
        except:
            service['status'] = 500

    print(services)
    return render_template('index.html', services=services)

if __name__ == "__main__":
    app.run(port=8000, host="127.0.0.1")
