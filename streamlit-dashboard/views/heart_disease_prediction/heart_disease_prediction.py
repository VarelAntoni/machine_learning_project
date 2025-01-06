import streamlit as st
import pandas as pd
import pickle
import time
from PIL import Image

col1_heart, col2_heart, col3_heart = st.columns([0.25,2.5,0.25], gap="small", vertical_alignment="center")

with col1_heart:
    st.write('\n')
with col2_heart:
    def heart():

        st.write("""
        ## Heart Disease Prediction Machine Learning Application
        """)
        st.write("""
        Data obtained from the [Heart Disease dataset](https://archive.ics.uci.edu/dataset/45/heart+disease) by UCIML.
        """)

        img = Image.open("./heart-disease.jpg")
        st.image(img, width=500)

        st.write('### User Input Features:')
         
        # Collects user input features into dataframe
        uploaded_file = st.file_uploader("Upload your input CSV file", type=["csv"])
        if uploaded_file is not None:
                input_df = pd.read_csv(uploaded_file)
        else:
            def user_input_features():
                st.subheader('Manual Input')
                cp = st.slider('Chest pain type', 1, 4, 2)
                if cp == 1.0:
                    wcp = "Chest pain caused by angina."
                elif cp == 2.0:
                    wcp = "Unstable chest pain, possibly angina."
                elif cp == 3.0:
                    wcp = "Severe unstable chest pain, likely angina."
                else:
                    wcp = "Chest pain not related to heart issues."
                st.write("The type of chest pain experienced by the patient:", wcp)
                thalach = st.slider("Maximum heart rate achieved", 71, 202, 80)
                slope = st.slider("ST segment elevation or depression on an electrocardiogram (ECG)", 0, 2, 1)
                oldpeak = st.slider("How much the ST segment is depressed or lowered", 0.0, 6.2, 1.0)
                exang = st.slider("Exercise induced angina", 0, 1, 1)
                ca = st.slider("Number of major vessels", 0, 3, 1)
                thal = st.slider("Thallium test results", 1, 3, 1)
                sex = st.selectbox("Gender", ('Woman', 'Man'))
                sex = 0 if sex == "Woman" else 1
                age = st.slider("Age", 29, 77, 30)
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
                features = pd.DataFrame(data, index=[0])
                return features
                
            input_df = user_input_features()
            
            
        if st.button('Predict!'):
            df = input_df
            st.write(df)
            with open("./generate_heart_disease.pkl", 'rb') as file:
                loaded_model = pickle.load(file)
            prediction = loaded_model.predict(df)
            result = ['Did Not Have Heart Disease' if prediction == 0 else 'Have Heart Disease']
            st.subheader('Prediction:')
            output = str(result[0])
            with st.spinner('Wait for it...'):
                time.sleep(4)
                st.success(f"Prediction of this app is: {output}")

    heart()

    with col3_heart:
        st.write('\n')
