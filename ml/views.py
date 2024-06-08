from django.shortcuts import render
from django.http import JsonResponse
import joblib
import pandas as pd
from menu.models import Recipe
from cart.models import Review
# Load the model at the start
model = joblib.load('../recommendation_system.joblib')

def predict(request):
    # Example data extraction, you need to adjust based on your actual use case
    user_interactions = list(Review.objects.all().values())
    recipes = list(Recipe.objects.all().values())
    
    # Convert data to DataFrame or the format your model expects
    interactions_df = pd.DataFrame(user_interactions)
    recipes_df = pd.DataFrame(recipes)

    # Use the model to make predictions
    predictions = model.predict(interactions_df)  # Adjust based on your model's input requirements

    return JsonResponse({'predictions': predictions.tolist()})
