from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the saved model
model = pickle.load(open('savedmodel.pkl', 'rb'))

@app.route('/')
def home():
    result = ''
    return render_template('index.html', result=result)

@app.route('/predict', methods=['POST'])
def predict():
    # Get values from form and convert to float
    sepal_length = float(request.form['sepal_length'])
    sepal_width = float(request.form['sepal_width'])
    petal_length = float(request.form['petal_length'])
    petal_width = float(request.form['petal_width'])

    # Prepare input for prediction (2D array)
    input_features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])

    # Make prediction
    result = model.predict(input_features)[0]

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)