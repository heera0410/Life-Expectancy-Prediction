#import the libraries
from flask import Flask,render_template,request
import pickle

# create an instance of flask class and __name__ is a special variable points to the __main__ when the script runs
app=Flask(__name__)

# load the trained model
model=pickle.load(open('model.pkl','rb'))


@app.route('/')
def main():
    ''' This function will render the main.html file at home page ie localhost:5000 since it routes to /'''
    return render_template('main.html')

@app.route('/predict',methods=['post'])
def predict():
    '''This function gets the form values ,converts the string into int or float accordingly and appends it to the features list 
       which then passed to the predict function as parameter and the result is displayed in the footer of the same page'''
    features=[]
    for i in request.form.values():
        try:
            features.append(int(i))
        except:
            features.append(float(i))
    prediction=model.predict([features])
    return render_template('main.html',data='Life_expectancy is {:.2f}'.format(float(prediction)))

if __name__=='__main__':
    app.run()