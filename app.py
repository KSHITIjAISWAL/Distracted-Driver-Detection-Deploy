from flask import Flask , render_template, flash, request, redirect, url_for
import model as m
from werkzeug.utils import secure_filename
import os
# from gevent.pywsgi import WSGIServer

app = Flask(__name__)


app.secret_key = 'kshitij'

app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/", methods = ["POST"])
def upload_image():
    
    file = request.files['file']
    if file:
        driver_pred = m.detect(file)
        drp = driver_pred
        print(drp)
        return render_template('index.html',pred = drp)
		
if __name__ == "__main__":
    app.run(debug=True)
    # http_server = WSGIServer(('', 5000), app)
    # http_server.serve_forever()