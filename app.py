from flask import Flask,render_template
import getFHIR

app = Flask(__name__)

@app.route('/')
def launch():
    return render_template('index.html',
                           patient_example=getFHIR.getPatient(),
                           condition_example=getFHIR.getCondition())

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8080)
