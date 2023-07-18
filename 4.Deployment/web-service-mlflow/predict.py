import pickle
import mlflow
from flask import Flask, request, jsonify


RUN_ID = '682824de8ca349bc908f40268a891c34'
EXPERIMENT_VER = 2
mlflow.set_tracking_uri("http://127.0.0.1:5000")  # It's still necessary to add this on prediction scripts \
                                                  # unless you point directly to cloud location

#logged_model = f'runs:/{RUN_ID}/model'
logged_model = f's3://mlops-zoomcamp-taxi-data/models/{EXPERIMENT_VER}/{RUN_ID}/artifacts/model'  # This is to remove dependency on tracking server
model = mlflow.pyfunc.load_model(logged_model)


def prepare_features(ride):
    features = {}
    features['PU_DO'] = '%s_%s' % (ride['PULocationID'], ride['DOLocationID'])
    features['trip_distance'] = ride['trip_distance']
    return features


def predict(features):
    preds = model.predict(features)
    return float(preds[0])


app = Flask('duration-prediction')


@app.route('/predict', methods=['POST'])
def predict_endpoint():
    ride = request.get_json()

    features = prepare_features(ride)
    pred = predict(features)

    result = {
        'duration': pred,
        'model_version': RUN_ID
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)
