import streamlit as st
import pandas as pd
import os

col1, col2, col3, col4 = st.columns([0.3,1.7,1.75,0.25], gap="small", vertical_alignment="center")
with col1:
    st.write("\n")
with col2:
    if os.path.exists("streamlit-dashboard/assets/varel-pic.jpg"):
        st.image("streamlit-dashboard/assets/varel-pic.jpg", width=400)
with col3:
    st.title("Muhammad Varel Antoni", anchor="False")
    st.text("A passionate Data and AI enthusiast with a strong interest in machine learning, data analysis, and AI-driven innovation, I am an undergraduate Information Technology student at the University of Brawijaya. I also serve as the Manager of Organizational Development at the Human Resource Society of Renewable Energy UB, where I apply my skills to drive organizational growth and sustainability.")
    add_selectitem = st.selectbox("Want to open about?", ("Education", "Experience", "Awards and Certifications"))
with col4:
    st.write("\n")

   
#Education
def education():
    st.write("\n")
    col1_edu, col2_edu, col3_edu = st.columns([0.25,2.5,0.25], gap="small", vertical_alignment="center")

    with col1_edu:
        st.write("\n")
    with col2_edu:
        st.subheader("🎓 Education")
        st.write("\n")
        st.markdown("##### **Brawijaya University - Indonesia**")
        st.write(
            """
            Majoring in Information Technology 
            - Specialization in Data Science and Artificial Intelligence.
            - Focus on Programming for Data Analysis and Software Development.
            - Academics Project :
            1. **Brain Tumor Prediction** : Built a Convolutional Neural Network (CNN) model for
            classifying MRI brain scans to detect tumors.
            2. **Plane Price Prediction** : Built a regression model to predict plane prices based on
            various features such as Max speed Knots, Empty weight lbs, Price and others.
            """
        )
        
        st.write("\n")
        st.markdown("##### **Machine Learning & AI Bootcamp at DQLab**")
        st.write(
            """
            Best Participant
            - Learn about Machine Learning and Deep Learning.
            - Deploying a Machine Learning Model to a Dashboard.
            - Capstone Project :
            1. **Heart Disease Prediction** : Developed a classification model with optimized performance
            through hyperparameter tuning and successfully deployed it using Streamlit for
            interactive visualization and user engagement

            """
        )
    with col3_edu:
        st.write("\n")

#Education
def experience():
    st.write("\n") 
    col1_exp,col2_exp, col3_exp = st.columns([0.25,2.5,0.25], gap="small", vertical_alignment="center")

    with col1_exp:
        st.write("\n")
    with col2_exp:
        st.subheader("💫 Experience")
        st.write("\n")
        st.markdown("##### **Project-Based Virtual Intern: Home Credit x Rakamin Academy**")
        st.write(
            """
            I work as a data scientist, focusing on predicting credit scores using various regression models.
            In this role, I analyze and prepare data, apply different regression techniques, and develop
            models to make accurate credit score predictions. I work with many datasets to continuously
            improve the models and ensure that the insights gained from the predictions are effectively
            used in shaping business strategies.
            - Final Task Project :
                - **Home Credit Scorecard Model** : This project analyzes creditworthiness using multiple
                datasets to improve results, employing Regression Models and Random Forest,
                achieving an accuracy of 0.97+. The model identifies key factors such as payment
                history, supporting more accurate and efficient credit decision-making.

            """
        )

        st.write("\n")
        st.markdown("#### **📈 Organization Experience**")
        st.write(
            """
            - **Society of Renewable Energy** - Brawijaya University (Associates  of Human Resources)
            - **Society of Renewable Energy** - Brawijaya University (Manager of Organizational Development at Human Resources)

            """
        )

        st.write("\n")
        st.markdown("#### **📈 Volunteer Experience**")
        st.write(
            """
            - **Study With SRE x Lawnergy Talks 2024** - SRE UB 2024 (Project Officer)
            - **Company Visit & Power Plant Visit SRE UB 2024** - SRE UB 2024 (Event Coordinator)
            - **Filkompreneur 2023** - BEM FILKOM 2023 (Public Relation Staff) 
            - **Leader of Tomorrow 5.0 2023** - BEM FILKOM UB 2023 (Public Relation Staff)
            - **Synergy of Symphony & Shaping The Future 2023** - KBMDSI UB 2023 (Field Operations Division Staff)
            - **Inaugurasi x Dekan Cup FILKOM UB 2022** - BEM FILKOM UB 2022 (Staff Divisi Keamanan)
            """
        )
    with col3_exp:
        st.write("\n")

def award():
    st.write("\n") 
    col1_awr,col2_awr, col3_awr = st.columns([0.25,2.5,0.25], gap="small", vertical_alignment="center")

    with col1_awr:
        st.write("\n")
    with col2_awr:
        st.subheader("🏆 Awards and Certifications")
        st.write("\n")
        st.markdown("#### **🏅 Awards**")
        st.write(
            """
            - First Place ICT Business Idea Competition ITCC 2024
            - First Place Business Plan Pokja Scientific Competition 2024

            [Certificate](https://drive.google.com/file/d/1qgfkU26JC75gRbWdrRkQRTXZlyRIDwUu/view?usp=drive_link)
            """
        )

        st.write("\n")
        st.markdown("#### **📜 Certifications**")
        st.write(
            """
            - Certificate of Achievement - Home Credit Indonesia Data Science Project Based Internship Program
            - Bootcamp Machine Learning & AI for Beginner Batch 14 DQLab
            - Accenture North America - Data Analytics and Visualization Job Simulation Forage
            - ASEAN Data Science Explorers 2024 Enablement Session - SAP Analytics Cloud and SAP Build Apps Online Training Session
            - Belajar Dasar Data Science Dicoding
            - 8+ Certificates of SQL from DQLab

            [Certificate](https://drive.google.com/file/d/1cd7Xr2C_jNpiUS1i8zF2CUSfB-pjcZNH/view?usp=drive_link)
            """
        )

    with col3_awr:
        st.write("\n")


if add_selectitem == "Education":
    education()
elif add_selectitem == "Experience":
    experience()
elif add_selectitem == "Awards and Certifications":
    award()
    

        

