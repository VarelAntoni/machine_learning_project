import streamlit as st
import pandas as pd
import pickle
import time
from PIL import Image


st.set_page_config(page_title="Halaman Modelling", layout="wide")
st.write("""
# Welcome to my Machine Learning Dashboard

This dashboard created by : [@muhammadvarelantoni](www.linkedin.com/in/muhammadvarelantoni)
""")

add_selectitem = st.sidebar.selectbox("Want to open about?", ("Heart Disease!", "Iris Species!"))

def heart():
    st.write("""
    This app predicts the **Heart Disease**

    Data obtained from the [Heart Disease dataset](https://archive.ics.uci.edu/dataset/45/heart+disease) by UCIML.
    """)
    st.sidebar.header('User Input Features:')
    # Collects user input features into dataframe
    uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])
    if uploaded_file is not None:
        input_df = pd.read_csv(uploaded_file)
    else:
        def user_input_features():
            st.sidebar.header('Manual Input')
            cp = st.sidebar.slider('Chest pain type', 1,4,2)
            if cp == 1.0:
                wcp = "Chest pain caused by angina."
            elif cp == 2.0:
                wcp = "Unstable chest pain, possibly angina."
            elif cp == 3.0:
                wcp = "Severe unstable chest pain, likely angina."
            else:
                wcp = "Chest pain not related to heart issues."
            st.sidebar.write("The type of chest pain experienced by the patient.", wcp)
            thalach = st.sidebar.slider("Maximum heart rate achieved", 71, 202, 80)
            slope = st.sidebar.slider("ST segment elevation or depression on an electrocardiogram (ECG).", 0, 2, 1)
            oldpeak = st.sidebar.slider("How much the ST segment is depressed or lowered.", 0.0, 6.2, 1.0)
            exang = st.sidebar.slider("Exercise induced angina", 0, 1, 1)
            ca = st.sidebar.slider("Number of major vessels", 0, 3, 1)
            thal = st.sidebar.slider("Thallium test results.", 1, 3, 1)
            sex = st.sidebar.selectbox("Gender", ('Woman', 'Man'))
            if sex == "Woman":
                sex = 0
            else:
                sex = 1
            age = st.sidebar.slider("Usia", 29, 77, 30)
            data = {'cp': cp,
                    'thalach': thalach,
                    'slope': slope,
                    'oldpeak': oldpeak,
                    'exang': exang,
                    'ca':ca,
                    'thal':thal,
                    'sex': sex,
                    'age':age}
            features = pd.DataFrame(data, index=[0])
            return features
        
    input_df = user_input_features()
    img = Image.open("heart-disease.jpg")
    st.image(img, width=500)
    if st.sidebar.button('Predict!'):
        df = input_df
        st.write(df)
        with open("generate_heart_disease.pkl", 'rb') as file:
            loaded_model = pickle.load(file)
        prediction = loaded_model.predict(df)
        result = ['Did Not Have Heart Disease' if prediction == 0 else 'Have Heart Disease']
        st.subheader('Prediction: ')
        output = str(result[0])
        with st.spinner('Wait for it...'):
            time.sleep(4)
            st.success(f"Prediction of this app is {output}")

if add_selectitem == "Heart Disease!":
    heart()
elif add_selectitem == "Iris Species!":
    st.write("Prediction of Iris Species under maintenance")

