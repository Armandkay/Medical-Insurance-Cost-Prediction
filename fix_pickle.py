import pickle
import os

# Define paths
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "linear_regression"))
MODEL_PATH = os.path.join(BASE_DIR, "best_model.pkl")
SCALER_PATH = os.path.join(BASE_DIR, "scaler.pkl")

# Function to reload and resave pickle files
def fix_pickle_file(file_path):
    try:
        # Load the file
        with open(file_path, "rb") as f:
            obj = pickle.load(f)
        
        # Resave the file
        with open(file_path, "wb") as f:
            pickle.dump(obj, f)
        
        print(f"Fixed: {file_path}")

    except Exception as e:
        print(f"Error fixing {file_path}: {e}")

# Run the fix for both model and scaler
if __name__ == "__main__":
    fix_pickle_file(MODEL_PATH)
    fix_pickle_file(SCALER_PATH)
