import pandas as pd
import numpy as np

# Generate synthetic data
np.random.seed(42)
num_samples = 1000
calories = np.random.uniform(1500, 3000, num_samples)
protein = calories * 0.075  # Assuming 7.5% of calories should be protein
fat = calories * 0.30  # Assuming 30% of calories should be fat
carbs = calories * 0.55  # Assuming 55% of calories should be carbs

# Create DataFrame
nutrition_data = pd.DataFrame({
    'calories': calories,
    'protein': protein,
    'fat': fat,
    'carbs': carbs
})

# Save to CSV
nutrition_data.to_csv('nutrition_data.csv', index=False)
print("Nutrition data saved to 'nutrition_data.csv'")
