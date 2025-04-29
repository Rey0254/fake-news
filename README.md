# Fake News Detector - Proyecto MLOps

Este proyecto implementa un modelo de Machine Learning para detectar noticias falsas (Fake News) a partir de texto libre.

La aplicación es desplegada mediante **Streamlit**, empaquetada en un contenedor **Docker**, y automatizada usando **GitHub Actions**.

---

## Ejecución Local

1. Instala las dependencias:

```bash
pip install -r requirements.txt
```

2. Ejecuta la aplicación:

```bash
streamlit run app.py
```

Accede en: [http://localhost:8501](http://localhost:8501)

---

## Construcción y ejecución con Docker

1. Construir la imagen:

```bash
docker build -t fake-news-detector .
```

2. Ejecutar el contenedor:

```bash
docker run -p 8501:8501 fake-news-detector
```

---

## Automatización con GitHub Actions

El flujo de trabajo (`deploy.yml`) realiza los siguientes pasos automáticamente al hacer push en GitHub:
- Instala dependencias.
- Reentrena el modelo (`train.py`).
- Construye la imagen Docker.
- Publica la imagen en DockerHub.

---

## Manejo de Credenciales

Se utilizan **Secrets** en GitHub para proteger la autenticación en DockerHub:
- `DOCKER_USERNAME`
- `DOCKER_PASSWORD`

---

## Variables de Entrada y Salida del Modelo

| Tipo | Descripción |
|:----|:------------|
| Entrada | Texto libre que representa una noticia. |
| Salida | Predicción: `1` para noticia Falsa (Fake News), `0` para noticia Verdadera. |

---

##  Autor

- Reychell Segura

---



