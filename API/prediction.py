# import pickle
# import numpy as np
# from fastapi import FastAPI
# from pydantic import BaseModel
# import uvicorn
# import os

# # Define paths to model and scaler
# BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))  # Get INTEGRATION folder
# MODEL_PATH = os.path.join(BASE_DIR, "linear_regression", "best_model.pkl")
# SCALER_PATH = os.path.join(BASE_DIR, "linear_regression", "scaler.pkl")

# # Load the trained model and scaler
# try:
#     with open(MODEL_PATH, "rb") as model_file:
#         model = pickle.load(model_file)

#     with open(SCALER_PATH, "rb") as scaler_file:
#         scaler = pickle.load(scaler_file)
# except Exception as e:
#     raise RuntimeError(f"Error loading model or scaler: {e}")

# # Initialize FastAPI app
# app = FastAPI(title="Medical Insurance Cost Prediction API")

# # Define input schema
# class InsuranceInput(BaseModel):
#     age: int
#     sex: str  # "male" or "female"
#     bmi: float
#     children: int
#     smoker: str  # "yes" or "no"
#     region: str  # "northeast", "northwest", "southeast", "southwest"

# # Preprocessing function
# def preprocess_input(data: InsuranceInput):
#     try:
#         # Convert categorical values
#         sex_map = {"male": 1, "female": 0}
#         smoker_map = {"yes": 1, "no": 0}
#         region_map = {"northeast": 0, "northwest": 1, "southeast": 2, "southwest": 3}

#         processed_data = [
#             data.age,
#             sex_map.get(data.sex.lower()),  # Ensure lowercase input
#             data.bmi,
#             data.children,
#             smoker_map.get(data.smoker.lower()),  # Ensure lowercase input
#             region_map.get(data.region.lower())  # Ensure lowercase input
#         ]

#         if None in processed_data:
#             raise ValueError("Invalid categorical value provided.")

#         # Scale input
#         processed_data = scaler.transform([processed_data])
#         return processed_data
#     except Exception as e:
#         raise ValueError(f"Error preprocessing input: {e}")

# # Prediction endpoint
# @app.post("/predict")
# def predict(input_data: InsuranceInput):
#     try:
#         processed_data = preprocess_input(input_data)
#         prediction = model.predict(processed_data)
#         return {"predicted_insurance_cost": float(prediction[0])}  # Ensure JSON serializable
#     except Exception as e:
#         return {"error": str(e)}

# # Run the app
# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)
import pickle
import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import os

# Define paths to model and scaler
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))  # Get INTEGRATION folder
# MODEL_PATH = os.path.join(BASE_DIR, "linear_regression", "best_model.pkl")
# SCALER_PATH = os.path.join(BASE_DIR, "linear_regression", "scaler.pkl")
MODEL_PATH = os.path.join(BASE_DIR, "linear_regression", "best_model.pkl")
SCALER_PATH = os.path.join(BASE_DIR, "linear_regression", "scaler.pkl")



# Reload and resave the .pkl files to fix potential corruption
try:
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)
    with open(SCALER_PATH, "rb") as f:
        scaler = pickle.load(f)
    
    with open(MODEL_PATH, "wb") as f:
        pickle.dump(model, f)
    with open(SCALER_PATH, "wb") as f:
        pickle.dump(scaler, f)

except Exception as e:
    raise RuntimeError(f"Error loading or resaving model/scaler: {e}")

# Initialize FastAPI app
app = FastAPI(title="Medical Insurance Cost Prediction API")

# Define input schema
class InsuranceInput(BaseModel):
    age: int
    sex: str  # "male" or "female"
    bmi: float
    children: int
    smoker: str  # "yes" or "no"
    region: str  # "northeast", "northwest", "southeast", "southwest"

# Preprocessing function
def preprocess_input(data: InsuranceInput):
    try:
        # Convert categorical values
        sex_map = {"male": 1, "female": 0}
        smoker_map = {"yes": 1, "no": 0}
        region_map = {"northeast": 0, "northwest": 1, "southeast": 2, "southwest": 3}

        processed_data = [
            data.age,
            sex_map.get(data.sex.lower()),  # Ensure lowercase input
            data.bmi,
            data.children,
            smoker_map.get(data.smoker.lower()),  # Ensure lowercase input
            region_map.get(data.region.lower())  # Ensure lowercase input
        ]

        if None in processed_data:
            raise ValueError("Invalid categorical value provided.")

        # Scale input
        processed_data = scaler.transform([processed_data])
        return processed_data
    except Exception as e:
        raise ValueError(f"Error preprocessing input: {e}")

# Prediction endpoint
@app.post("/predict")
def predict(input_data: InsuranceInput):
    try:
        processed_data = preprocess_input(input_data)
        prediction = model.predict(processed_data)
        return {"predicted_insurance_cost": float(prediction[0])}  # Ensure JSON serializable
    except Exception as e:
        return {"error": str(e)}

# Run the app
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
