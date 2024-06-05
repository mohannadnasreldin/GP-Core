import joblib
import recommendation_system

# Assuming 'model' is your trained machine learning model
joblib_file = "recommendation_system.joblib"
joblib.dump(recommendation_system, joblib_file)
