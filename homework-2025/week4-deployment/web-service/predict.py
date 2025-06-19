import pickle

from flask import Flask, request, jsonify

with open ('model.bin', 'rb') as f_in:
    (dv, model) = pickle.load(f_in)

def prepare_data(data):
    features = {}
    features['PU_DO'] = '%s_%s' % (data['PULocationID'], data['DOLocationID'])
    features['trip_distance'] = data['trip_distance']
    return features

def predict(data):
    X = dv.transform(data)
    y_pred = model.predict(X)
    return y_pred


app = Flask('duration-predictor')

@app.route('/predict', methods=['POST'])
def predict_ride():
    ride = request.get_json()
    features = prepare_data(ride)
    prediction = predict(features)
    result ={
        'duration': prediction[0],
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9696)