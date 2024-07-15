import streamlit as st
import numpy as np
import pickle
import os

# Function to load model with error handling
def load_model(file_name):
    try:
        with open(file_name, 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        st.error(f"Model file '{file_name}' not found.")
        return None
    except Exception as e:
        st.error(f"An error occurred while loading the model '{file_name}': {e}")
        return None

# Load the models
model_protein = load_model('model_protein.pkl')
model_fat = load_model('model_fat.pkl')
model_carbs = load_model('model_carbs.pkl')

# Check if models are loaded successfully
if model_protein is None or model_fat is None or model_carbs is None:
    st.stop()
st.set_theme('light')

# Custom CSS for styling
st.markdown("""
    <style>
    body {
      font-family: 'Arial', sans-serif;
      background-color: #f4f4f4;
    }
    header {
      background-color: #2ecc71;
      color: #ffffff;
      padding: 10px 0;
      text-align: center;
      width: 100%;
    }
    footer {
      background-color: #2ecc71;
      color: #ffffff;
      padding: 10px 0;
      text-align: center;
      width: 100%;
      margin-top: auto;
    }
    main {
      display: flex;
      justify-content: space-around;
      flex-wrap: wrap;
      margin-top: 20px;
    }
    .calculator-container {
      background-color: #ffffff;
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
      padding: 20px;
      border-radius: 8px;
      text-align: center;
      width: 45%;
      margin-bottom: 20px;
    }
    h1 {
      color: #333333;
    }
    label {
      display: block;
      margin-top: 10px;
      font-weight: bold;
      color: #555555;
    }
    input {
      width: calc(100% - 20px);
      padding: 10px;
      margin-top: 5px;
      margin-bottom: 15px;
      box-sizing: border-box;
      border: 1px solid #ccc;
      border-radius: 4px;
    }
    button {
      background-color: #2ecc71;
      color: #ffffff;
      padding: 10px 20px;
      border: none;
      border-radius: 4px;
      cursor: pointer;
      font-size: 16px;
    }
    button:hover {
      background-color: #27ae60;
    }
    .result-container {
      margin-top: 20px;
      font-weight: bold;
      color: #333333;
    }
    .info-container {
      background-color: #ffffff;
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
      padding: 20px;
      border-radius: 8px;
      text-align: left;
      width: 80%;
      max-width: 800px;
    }
    p {
      color: #333333;
      margin-bottom: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown('<header><h1>Health & Nutrition Hub</h1></header>', unsafe_allow_html=True)

# Main content
st.markdown('<main>', unsafe_allow_html=True)

# BMI Calculator
st.markdown('<div class="calculator-container">', unsafe_allow_html=True)
st.header('BMI Calculator')
weight = st.number_input('Weight (kg):', min_value=0.0, format="%.2f")
height = st.number_input('Height (cm):', min_value=0.0, format="%.2f")

if weight > 0 and height > 0:
    height_m = height / 100
    bmi = weight / (height_m ** 2)
    st.write(f'Your BMI: {bmi:.2f}')
    if bmi < 18.5:
        st.write('Underweight')
    elif 18.5 <= bmi < 24.9:
        st.write('Normal weight')
    elif 25 <= bmi < 29.9:
        st.write('Overweight')
    else:
        st.write('Obese')

st.markdown('</div>', unsafe_allow_html=True)

# Nutrition Calculator
st.markdown('<div class="calculator-container">', unsafe_allow_html=True)
st.header('Nutritional Calculator')
calories = st.number_input('Daily Caloric Intake (kcal):', min_value=0.0, format="%.2f")

if calories > 0:
    protein_needed = model_protein.predict(np.array(calories).reshape(-1, 1))[0]
    fat_needed = model_fat.predict(np.array(calories).reshape(-1, 1))[0]
    carbs_needed = model_carbs.predict(np.array(calories).reshape(-1, 1))[0]

    st.write(f'Protein: {protein_needed:.2f} grams')
    st.write(f'Fat: {fat_needed:.2f} grams')
    st.write(f'Carbohydrates: {carbs_needed:.2f} grams')

st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</main>', unsafe_allow_html=True)

# Food Security and Nutrition Facts
st.markdown('<div class="info-container">', unsafe_allow_html=True)
st.header('Food Security and Nutrition Facts')

facts = [
    "Malnutrition affects people of all ages and is a major global health concern.",
    "Access to a diverse and balanced diet is crucial for proper nutrition.",
    "Food security is not only about the quantity of food but also the quality and safety of the food consumed.",
    "Sustainable agriculture practices play a vital role in ensuring long-term food security.",
    "Global cooperation is essential to address issues such as food distribution, climate change, and poverty, which impact food security.",
    "Undernutrition and overnutrition are both forms of malnutrition and pose significant health risks.",
    "Micronutrient deficiency, also known as hidden hunger, can lead to various health problems.",
    "Food insecurity is often linked to economic instability and social inequalities.",
    "Efforts to achieve Zero Hunger (SDG 2) aim to eliminate hunger, improve food security, and promote sustainable agriculture globally.",
    "Promoting awareness and education about nutrition is crucial for building healthy and resilient communities."
]

random_fact = np.random.choice(facts)
st.write(f'<p>{random_fact}</p>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown('<footer><p>Health & Nutrition Hub &copy; 2024</p></footer>', unsafe_allow_html=True)
