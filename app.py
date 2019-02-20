from flask import Flask,render_template
import getFHIR

app = Flask(__name__)

'''
The app route parameter specifies when each function in app.py will be called. Since this is our initial function we
want called, we will designate it to run when users navigate to the base url of our app. In this example the base 
will be http://0.0.0.0:8080/ but you could specify other routes such as http://0.0.0.0:8080/details or 
http://0.0.0.0:8080/list to launch additional views for your app with each function rendering different templates.
'''
@app.route('/')
def launch():
    '''
    Launches our initial view by rendering dashboard.html and calling each method from our imported getFHIR.py file.
    The return from each method will populate the dynamic variables designated by double curly braces in the HTML.
    '''
    return render_template('index.html',
                           patient_example=getFHIR.getPatient(),
                           condition_example=getFHIR.getCondition())

#Allows you to run this file with the command 'python app.py' and launch the Flask server on the designated host and port.
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8080)
