from flask import (
     Flask, 
     request, 
     render_template)
from model import sorayomi

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['GET', 'POST'])
def result():
    try:
        if request.method == 'POST':
            atmo = int(request.form['atmo'])
            input_length = request.form['input_length']
            a = request.form['a']
            author,title,table = sorayomi(atmo,input_length,a)
            return render_template('result.html',author = author ,title = title ,table = table)
    except Exception as e:
        return render_template('page_not_found.html')

@app.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('about.html')
        
if __name__ == '__main__':
  app.run(debug=True)