import joblib
import os
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import subprocess

# Datos
X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

# Modelo
model = RandomForestClassifier(n_estimators=100, max_depth=3, random_state=42)
model.fit(X_train, y_train)

# Evaluar el modelo
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"\nPrecisión del modelo: {accuracy:.4f}")
print("\nInforme de clasificación:")
print(classification_report(y_test, y_pred))

# Crear directorio si no existe
os.makedirs("models", exist_ok=True)

# Guardar modelo
model_path = "models/model.pkl"
joblib.dump(model, model_path)
print(f"\nModelo guardado en {model_path}")

# Versionar con DVC
try:
    subprocess.run(["dvc", "add", model_path], check=True)
    print("Modelo versionado con DVC correctamente.")
    
    # Agregar .gitignore para evitar que Git rastree el archivo grande
    subprocess.run(["git", "add", ".gitignore", "models.dvc"], check=True)
    subprocess.run(["git", "commit", "-m", "Actualización del modelo con DVC"], check=False)
    print("Cambios registrados en Git.")
except Exception as e:
    print(f"Error al versionar con DVC: {e}")
