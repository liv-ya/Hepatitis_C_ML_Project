from flask import Flask, request, render_template
import pickle

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
   
    wbc = float(request.form.get('wbc'))
    rbc = request.form.get('rbc')
    plat = request.form.get('plat')
    alt1 = float(request.form.get('alt1'))
    alt4 = float(request.form.get('alt4'))
    alt12 = float(request.form.get('alt12'))
    alt48 = float(request.form.get('alt48'))
    rnabase = float(request.form.get('rnabase'))
    rna4 = float(request.form.get('rna4'))
    rnaeot = float(request.form.get('rnaeot'))
    

    input_features = [[wbc,rbc,plat,alt1,alt4,alt12,alt48,rnabase,rna4,rnaeot]]

    # Load the model and make a prediction
    with open('rf_sample.pkl', 'rb') as model_file:
        rf = pickle.load(model_file)
        input_features=pandas.DataFrame(input_features, columns=['WBC', 'RBC', 'Plat', 'ALT 1', 'ALT4','ALT 12', 'ALT 48', 'RNA Base', 'RNA 4','RNA EOT'])
        #print(input_features)
        prediction = rf.predict(input_features)
        result = prediction[0]

        return render_template('result.html', res=result)
   
if __name__ == '__main__':
    app.run(debug=True)
