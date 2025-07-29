# 🚀 End-to-End Machine Learning API

An end-to-end production-ready API that serves machine learning predictions with robust features including authentication, Redis caching, Prometheus monitoring, and Dockerized deployment. Built using **FastAPI**.

Demo Link: https://end-to-end-car-price-prediction.onrender.com

---

## 📚 Table of Contents

- [Project Overview](#project-overview)  
- [Features](#features)  
- [Project Structure](#project-structure)  
- [Setup Instructions](#setup-instructions)  
- [Running the Application](#running-the-application)  
- [API Endpoints](#api-endpoints)  
- [Authentication](#authentication)  
- [Model Training](#model-training)  
- [Caching](#caching)  
- [Monitoring](#monitoring)  
- [Deployment](#deployment)  
- [Additional Notes](#additional-notes)  

---

## 📌 Project Overview

This project provides an **End-to-End API** for serving machine learning predictions.  
Key components include:

- JWT-based authentication  
- Model inference using a pre-trained ML model  
- Redis caching for performance  
- Prometheus for real-time monitoring  
- Docker for deployment  

---

## ✨ Features

- ✅ **User Authentication** (JWT-based)  
- 🤖 **ML Model Serving** (`joblib` model)  
- ⚡ **Prediction Caching** (Redis)  
- 📝 **Logging Middleware**  
- 📊 **Prometheus Monitoring**  
- 📦 **Dockerized Deployment**

---

## 🏗️ Project Structure

```
End-to-End API/
│
├── app/
│   ├── api/                # API route definitions
│   │   ├── routes_auth.py
│   │   └── routes_predict.py
│   ├── cache/              # Redis caching logic
│   │   └── redis_cache.py
│   ├── core/               # Config, security, exception handling
│   │   ├── config.py
│   │   ├── dependencies.py
│   │   ├── exceptions.py
│   │   └── security.py
│   ├── middleware/         # Logging middleware
│   │   └── logging_middleware.py
│   ├── models/             # Trained ML model
│   │   └── model.joblib
│   ├── services/           # Model inference logic
│   │   └── model_service.py
│   └── main.py             # FastAPI app entry point
│
├── data/
│   └── car-details.csv     # Sample dataset
│
├── training/
│   ├── train_model.py      # Training script
│   └── train_utils.py
│
├── notebooks/
│   └── sample.ipynb        # EDA & prototyping
│
├── Dockerfile
├── docker-compose.yml
├── prometheus.yml
├── render.yaml
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 🔧 Prerequisites

- Python 3.8+
- Redis (locally or via Docker)
- Docker & Docker Compose (for containerized setup)

### 🛠️ Installation

```bash
# 1. Clone the Repository
git clone <repo-url>
cd End-to-End\ API

# 2. Create Virtual Environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install Dependencies
pip install -r requirements.txt

# 4. Set Up Environment Variables
# Create a `.env` file in app/ if needed

# Example .env
SECRET_KEY=your_secret_key
REDIS_URL=redis://localhost:6379/0
```

---

## 🚀 Running the Application

### 🧪 Option 1: Local Development

Start Redis server manually if not using Docker:
```bash
redis-server
```

Run the FastAPI app:
```bash
uvicorn app.main:app --reload
```

Access it at: [http://localhost:8000](http://localhost:8000)

---

### 🐳 Option 2: Docker Compose

```bash
docker-compose up --build
```

This will start:

- FastAPI application  
- Redis server  
- Prometheus server (if configured)  

---

## 📡 API Endpoints

| Method | Endpoint         | Description                        |
|--------|------------------|------------------------------------|
| POST   | `/auth/login`    | User authentication (returns JWT) |
| POST   | `/predict`       | Make prediction (JWT required)     |
| GET    | `/metrics`       | Prometheus metrics                 |

---

## 🔐 Authentication

- JWT is used for securing routes.  
- Use `/auth/login` to get the token.  
- Add token to protected requests using header:

```http
Authorization: Bearer <your_token>
```

---

## 🧠 Model Training

- Scripts are located in `training/`
- To retrain the model:
```bash
python training/train_model.py
```
- The trained model is saved to `app/models/model.joblib`

---

## ⚡ Caching

- Redis is used to cache predictions.
- Caching logic is implemented in `app/cache/redis_cache.py`.

---

## 📈 Monitoring

- Prometheus configuration is in `prometheus.yml`.
- Metrics exposed at: [http://localhost:8000/metrics](http://localhost:8000/metrics)

---

## 🚀 Deployment

### Docker

```bash
docker-compose up --build
```

### Render (Cloud)

- `render.yaml` provided for Render.com deployment.
- Setup environment variables in Render dashboard.

---

## 📝 Additional Notes

- 🧪 **Jupyter Notebooks**: For EDA and prototyping in `notebooks/`.
- 🧾 **Logging**: Custom middleware logs all incoming requests (`app/middleware/logging_middleware.py`).
- ⚙️ **Config**: Centralized settings in `app/core/config.py`.

---
