# app.py

import streamlit as st
import joblib

# Cargar modelo y vectorizador
model = joblib.load('model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

st.title("📰 Fake News Detector")
st.subheader("Ingrese una noticia para verificar si es verdadera o falsa")

user_input = st.text_area("Escribe aquí la noticia:", height=200)

if st.button("Verificar"):
    if user_input.strip() == "":
        st.warning("Por favor ingrese algún texto para analizar.")
    else:
        user_vector = vectorizer.transform([user_input])

        prediction = model.predict(user_vector)[0]

        # Mostrar el resultado
        if prediction == 1:
            st.error("🚨 ¡La noticia parece ser FALSA!")
        else:
            st.success("✅ La noticia parece ser VERDADERA.")

