import joblib

def test_model():
    model = joblib.load("models/model.joblib")
    assert model is not None
