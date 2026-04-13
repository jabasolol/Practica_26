import pandas as pd
from sklearn.linear_model import LogisticRegression
import joblib
import os

# Crear carpeta models si no existe
os.makedirs("models", exist_ok=True)

# Datos simples
data = pd.DataFrame({
    "text": ["good", "bad", "excellent", "poor"],
    "label": [1, 0, 1, 0]
})

X = data["text"]
y = data["label"]

# Entrenar modelo
model = LogisticRegression()
model.fit([[len(x)] for x in X], y)

# Guardar modelo
joblib.dump(model, "models/model.joblib")

print("Modelo entrenado correctamente")

crear train.py
