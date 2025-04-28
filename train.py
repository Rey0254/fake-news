
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib

# dataset pequeño de ejemplo
data = {
    "text": [
        "Breaking news: The president is dead!",
        "Exclusive: Cure for cancer discovered!",
        "Dog wins local marathon",
        "Aliens land in Central Park",
        "Economy shows strong growth",
        "Scientists find water on Mars",
        "Shocking secret diet that makes you lose 20kg in a week!",
        "Government plans new highway",
        "Man claims to time travel",
        "Local team wins championship"
    ],
    "label": [1, 1, 0, 1, 0, 0, 1, 0, 1, 0]  # 1 = Fake news, 0 = Real news
}

df = pd.DataFrame(data)

X = df["text"]
y = df["label"]

# Separar en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer()

X_train_vectors = vectorizer.fit_transform(X_train)
X_test_vectors = vectorizer.transform(X_test)

# Crear y entrenar modelo
model = LogisticRegression()
model.fit(X_train_vectors, y_train)

joblib.dump(model, 'model.pkl')
joblib.dump(vectorizer, 'vectorizer.pkl')

print("Modelo entrenado y guardado exitosamente.")
