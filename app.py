from flask import Flask, render_template, request
from flask import Flask, render_template, request, redirect, url_for, session
from datetime import timedelta

import pandas as pd
import joblib

app = Flask(__name__)
app.secret_key = "asdfgh123456sdfghjhgu765edcvhy654"  # Required for using session
app.permanent_session_lifetime = timedelta(minutes=5)
# Load the trained model
model = joblib.load('artifacts/model_trainer/model.joblib')
model_columns = joblib.load('artifacts/model_trainer/model_columns.joblib')
df= pd.read_csv('artifacts/data_ingestion/Car details v3.csv')
car_names = sorted(list(set(df['name'].unique().tolist())))

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        # Collect form data
        input_data = {
            'year': int(request.form['year']),
            'km_driven': int(request.form['km_driven']),
            'fuel': request.form['fuel'],
            'seller_type': request.form['seller_type'],
            'transmission': request.form['transmission'],
            'owner': request.form['owner'],
            'mileage': float(request.form['mileage']),
            'engine': float(request.form['engine']),
            'max_power': float(request.form['max_power']),
            'torque': float(request.form['torque']),
            'seats': float(request.form['seats']),
            'name': request.form.get('car_name')
        }

        # Convert to DataFrame and perform one-hot encoding
        df = pd.DataFrame([input_data])
        df = pd.get_dummies(df)  # Ensure same preprocessing
        # model_columns = joblib.load('artifacts/model_trainer/model.joblib')
        
        
        df = df.reindex(columns=model_columns, fill_value=0)

        # Predict
        prediction = round(model.predict(df)[0], 2)

        session['prediction'] = prediction

        return redirect(url_for('index'))  # 🚀 Redirect to GET method

    # GET method
    prediction = session.pop('prediction', None)  # 🔁 Show once, then forget

    return render_template('index.html', prediction=prediction , car_names = car_names ) 

if __name__ == '__main__':
    app.run(debug=True)
