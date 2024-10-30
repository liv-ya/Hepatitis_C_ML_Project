from flask import Flask, request, render_template
import pickle
import random

import pandas


app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/input')
def home():
    return render_template('input_form.html')

@app.route('/result', methods=['POST'])
def result():
    # Collect and validate the input
   
    wbc = request.form.get('wbc')
    rbc = request.form.get('rbc')
    plat = request.form.get('plat')
    #ast1 = request.form.get('ast1')
    alt1 = request.form.get('alt1')
    alt4 = request.form.get('alt4')
    #alt36 = request.form.get('alt36')
    alt48 = request.form.get('alt48')
    rnabase = request.form.get('rnabase')
    rna4 = request.form.get('rna4')
    #rna12 = request.form.get('rna12')
    rnaeot = request.form.get('rnaeot')
    rnaef = request.form.get('rnaef')
    

    input_features = [[wbc,rbc,plat,alt1,alt4,alt48,rnabase,rna4,rnaeot,rnaef]]

    # Load the model and make a prediction
    with open('rf_last.pkl', 'rb') as model_file:
        rf = pickle.load(model_file)
        input_features=pandas.DataFrame(input_features, columns=['WBC', 'RBC', 'Plat', 'ALT 1', 'ALT4','ALT 48', 'RNA Base', 'RNA 4','RNA EOT','RNA EF'])
        #print(input_features)
        prediction = rf.predict(input_features)
        result = prediction[0]
        
        return render_template('result.html', res=result)
if __name__ == '__main__':
    app.run(debug=True)
