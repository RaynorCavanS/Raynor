from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

model_file = open('maternal_health_risk.pkl', 'rb')
model = pickle.load(model_file, encoding='bytes')

@app.route('/')

def index():
    return render_template('index.html', insurance_cost=0)

@app.route('/predict', methods=['POST'])
def predict():
    '''
    Predict the insurance cost based on user inputs
    and render the result to the html page
    '''
    Age, SystolicBP, DiastolicBP, BS, BodyTemp, HeartRate = [x for x in request.form.values()]

    data = []

    data.append(int(Age))
    data.append(int(SystolicBP))
    data.append(int(DiastolicBP))
    data.append(int(BS))
    data.append(int(BodyTemp))
    data.append(int(HeartRate))


    prediction = model.predict([data])
    if prediction==0 :
        output = "High  Risk"
    elif prediction==1 :
        output = "Low Risk"
    else :
        output = "Mid Risk"

    return render_template('index.html', prediction=output, Age=Age, SystolicBP=SystolicBP, DiastolicBP=DiastolicBP,BS=BS, BodyTemp=BodyTemp, HeartRate=HeartRate)


if __name__ == '__main__':
    app.run(debug=True)
