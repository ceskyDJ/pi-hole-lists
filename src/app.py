from flask import Flask, render_template, Response
from flask_caching import Cache

from risk_eshops import create_blocklist_risk_eshops

app = Flask(__name__)

cache = Cache(config={'CACHE_TYPE': 'SimpleCache'})
cache.init_app(app)

@app.route('/', strict_slashes=False)
def index():
    """
    Endpoint serving index with information about provided pi-hole lists

    :return: HTML code of index template
    """
    return render_template('index.html')

@app.route('/risk-eshops')
@cache.cached(timeout=43200)
def risk_eshops():
    """
    Endpoint serving a risk eshops pi-hole list

    :return: Risk eshops pi-hole list in a format accepted by pi-hole
    """
    content = create_blocklist_risk_eshops()

    return Response(content, mimetype='text/plain', content_type='text/plain; charset=utf-8')

if __name__ == '__main__':
    app.run(debug=True)
