# Medical-Insurance-Cost-Prediction
# LINKS

link of deployement on render https://medical-insurance-cost-prediction-5gsk.onrender.com/docs

link to the notebook https://colab.research.google.com/drive/1TEHsanEjzOOkCmrB8BeqV-W0tPICEX7O#scrollTo=1z5EqdVSmqUM

# Medical Insurance Cost Prediction - Quick Guide
🔹 Project Overview
This project predicts medical insurance costs using Machine Learning (Linear Regression).
It includes:
 FastAPI backend for predictions

 Flutter frontend for user interaction
 
 Deployment on Render

📂 Project Structure

📂 integration/
│
├── 📂 linear_regression/       # ML model & scaler
│   ├── best_model.pkl
│   ├── scaler.pkl
│
├── 📂 API/                    # FastAPI backend
│   ├── prediction.py
│   ├── requirements.txt
│
├── 📂 insurance_app/          # Flutter frontend
│   ├── lib/main.dart
│   ├── pubspec.yaml
1️⃣ Setting Up the API
🔹 Install Dependencies

cd integration/API
pip install -r requirements.txt

🔹 Run API Locally

uvicorn prediction:app --reload
 Open http://127.0.0.1:8000/docs to test.

2️⃣ Deploying API on Render
🔹 Push Code to GitHub

git add .
git commit -m "Initial commit"
git push origin main
🔹 Deploy to Render
Build Command:

pip install -r requirements.txt
Start Command:

uvicorn API.prediction:app --host 0.0.0.0 --port $PORT
 Get live API URL and test in Swagger UI.

3️⃣ Running the Flutter App
🔹 Install Dependencies

cd integration/insurance_app
flutter pub get
🔹 Run in Browser

flutter run -d chrome
✅ Enter user details and click "Predict" to see results.

 Final Notes
 API is deployed on Render

 Flutter app runs predictions in the browser
 
 End-to-end insurance cost prediction system is ready! 🚀
