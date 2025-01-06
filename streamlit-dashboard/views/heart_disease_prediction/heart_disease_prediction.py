import streamlit as st
import pandas as pd
import pickle
import time
from PIL import Image
import os

# Layout for the page
col1_heart, col2_heart, col3_heart = st.columns([0.25, 2.5, 0.25], gap="small")

with col1_heart:
    st.write('\n')
with col2_heart:

    def heart():
        # Title and description
        st.write("""
        ## Heart Disease Prediction Machine Learning Application
        """)
        st.write("""
        Data obtained from the [Heart Disease dataset](https://archive.ics.uci.edu/dataset/45/heart+disease) by UCIML.
        """)

        # Dynamically construct the path to the image
        current_dir = os.path.dirname(os.path.abspath(__file__))  # Directory of the current script
        img_path = os.path.join(current_dir, "heart-disease.jpg")

        # Check if the image exists and display it
        if os.path.exists(img_path):
            img = Image.open(img_path)
            st.image(img, width=500)
        else:
            st.error("Image file not found. Please ensure 'heart-disease.jpg' is in the same directory.")

        st.write('### User Input Features:')

        # Collect user input features
        uploaded_file = st.file_uploader("Upload your input CSV file", type=["csv"])
        if uploaded_file is not None:
            try:
                input_df = pd.read_csv(uploaded_file)
            except Exception as e:
                st.error(f"Error reading the uploaded file: {e}")
                input_df = None
        else:
            # Manual input if no file is uploaded
            def user_input_features():
                st.subheader('Manual Input')
                cp = st.slider('Chest pain type', 1, 4, 2)
                chest_pain_desc = {
                    1: "Chest pain caused by angina.",
                    2: "Unstable chest pain, possibly angina.",
                    3: "Severe unstable chest pain, likely angina.",
                    4: "Chest pain not related to heart issues."
                }
                st.write("The type of chest pain experienced by the patient:", chest_pain_desc[cp])
                
                thalach = st.slider("Maximum heart rate achieved", 71, 202, 80)
                slope = st.slider("ST segment elevation or depression on an electrocardiogram (ECG)", 0, 2, 1)
                oldpeak = st.slider("How much the ST segment is depressed or lowered", 0.0, 6.2, 1.0)
                exang = st.slider("Exercise induced angina", 0, 1, 1)
                ca = st.slider("Number of major vessels", 0, 3, 1)
                thal = st.slider("Thallium test results", 1, 3, 1)
                sex = st.selectbox("Gender", ('Woman', 'Man'))
                sex = 0 if sex == "Woman" else 1
                age = st.slider("Age", 29, 77, 30)

                # Create a DataFrame for user input
                data = {
                    'cp': cp,
                    'thalach': thalach,
                    'slope': slope,
                    'oldpeak': oldpeak,
                    'exang': exang,
                    'ca': ca,
                    'thal': thal,
                    'sex': sex,
                    'age': age
                }
                return pd.DataFrame(data, index=[0])

            input_df = user_input_features()

        # Prediction button
        if st.button('Predict!'):
            if input_df is not None:
                st.write("### Input Data:")
                st.write(input_df)

                # Dynamically construct the model file path
                model_path = os.path.join(current_dir, "generate_heart_disease.pkl")

                # Check if the model file exists
                if os.path.exists(model_path):
                    try:
                        with open(model_path, 'rb') as file:
                            loaded_model = pickle.load(file)

                        # Make predictions
                        with st.spinner('Predicting...'):
                            time.sleep(4)  # Simulate prediction time
                            prediction = loaded_model.predict(input_df)
                            result = ['Did Not Have Heart Disease' if pred == 0 else 'Have Heart Disease' for pred in prediction]
                        
                        st.subheader('Prediction:')
                        st.success(f"Prediction of this app is: {result[0]}")
                    except Exception as e:
                        st.error(f"An error occurred during prediction: {e}")
                else:
                    st.error("Model file not found. Please ensure 'generate_heart_disease.pkl' is in the correct directory.")
            else:
                st.error("No valid input data provided. Please upload a file or enter data manually.")

    # Run the app
    heart()

with col3_heart:
    st.write('\n')
