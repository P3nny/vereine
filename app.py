from flask import Flask
from flask import render_template
from flask import abort
import json
import requests

app = Flask(__name__)

def get_json():
    r = requests.get('http://m.moers.de/www/verzeichnis-01.nsf/apijson.xsp/view-list-category1')
    data = r.json()
    return data

data = get_json()

def zahl():
    zahl = 1
    data = get_json()
    for object in data:
        object['ID'] = zahl
        zahl += 1
    return data

@app.route("/")
def index():
    template = 'index.html'
    object_list = zahl()
    return render_template(template, object_list=object_list)
        
            
@app.route('/<row_id>/')
def detail(row_id):
    template = 'detail.html'
    object_list = zahl()
    for row in object_list:
        if row['ID'] == int(row_id):
            return render_template(template, object=row, object_list=object_list)
    abort(404)
            
    
    
if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
