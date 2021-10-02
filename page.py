from flask import Flask, render_template, request
import globalvar
app = Flask(__name__)
@app.route('/', methods=['GET'])
def index():
    return render_template('main.html', text='')
@app.route('/formAction/', methods=['POST'])
def add_content():
    landname = request.form.get('landname')
    ret_str:str=replace(globalvar.html_txt,'<!--landlord-->',landname)
	return globalvar.html_txt
app.run(port=2020, host='0.0.0.0')