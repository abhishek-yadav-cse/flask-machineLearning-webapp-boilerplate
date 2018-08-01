#Import required python libraries
from flask import Flask, request, render_template, url_for

app = Flask(__name__)

#Defining home route
@app.route('/')
def home():
    # Any code for home page
    return render_template('home.html')

#Defining any further route if any
@app.route('/nextpage',methods=['POST','GET'])
    #Here you can write the logic for your machine learning model
    #The input from the form at home page can be used here and fed to the machine learning model
    #The result of the machine learning model can be output on nextpage.html file by passing them in the form of parameters.
    return render_template('nextpage.html'#some more parameter to be passed)


if __name__ == '__main__':
    app.debug = True

    app.run(host='0.0.0.0')
