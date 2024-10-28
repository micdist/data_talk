import pickle
from flask import Flask, request, jsonify


dv_file = 'dv.bin'
model_file = 'model1.bin'

def predict_single(customer, dv, model):
    X = dv.transform([customer])
    y_pred = model.predict_proba(X)[:,1]
    return y_pred[0]


with open(model_file, "rb") as f_in:
   model = pickle.load(f_in)

with open(dv_file, "rb") as f_in:
   dv = pickle.load(f_in)

app = Flask('churn')

@app.route('/predict', methods=['POST'])
def predict():
    customer = request.get_json()
    prediction = predict_single(customer,dv,model)
    churn = prediction >= 0.5
    
    result = {
        'churn_probability': float(prediction),
        'churn': bool(churn),
    }

    return jsonify(result)


@app.route('/', methods=['GET'])
def testing():
    return 'flask serving for HW 5'











if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=9696)