# iris-end-to-end-deploy

This project demonstrates a small machine learning workflow using the Iris dataset, containerized with Docker, and exposed via a FastAPI REST endpoint. The API accepts feature inputs and returns a prediction, which can be tested using Postman.

---

## 1. Project Structure

```
.
├── app.py
├── model.py
├── model.pkl
├── requirements.txt
└── Dockerfile
```

---

## 2. Requirements

- Docker installed (recommended)
- Optional (for local running without Docker):
  - Python 3.9+
  - pip

---

## 3. Training the Model (Automatic in Docker Build)

The model is trained using `model.py`. It loads the Iris dataset, trains a RandomForest model, and saves it as `model.pkl`.

When building the Docker image, this training step runs automatically.

---

## 4. Running with Docker (Recommended)

### **Build Image**

```bash
docker build -t iris-api .
```

### **Run Container**

```bash
docker run -p 8000:8000 iris-api
```

---

## 5. API Usage

### **Endpoint**

```
POST /predict
```

### **Request Body (JSON)**

```json
{
  "features": [5.1, 3.5, 1.4, 0.2]
}
```

### **Response**

```json
{
  "prediction": "setosa"
}
```

---

## 6. Testing With Postman

### Postman Collection

A Postman collection is included for quick testing located at:
Iris_Prediction.postman_collection.json

1. Open Postman
2. Select **POST**
3. Use URL:

   ```
   http://localhost:8000/predict
   ```

4. Set body to **raw → JSON**
5. Send sample input mentioned above

---

## 7. Running Without Docker (Local)

### **Install Dependencies**

```bash
pip install -r requirements.txt
```

### **Train Model**

```bash
python model.py
```

### **Start FastAPI**

```bash
uvicorn app:app --reload
```

---

## 8. API Documentation (Swagger)

Available automatically via FastAPI:

```
http://localhost:8000/docs
```

---

## 9. Notes

- Uses scikit-learn for modeling
- Uses FastAPI for REST
- Model trains once during Docker build
- Can be extended to custom datasets or models
