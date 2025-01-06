import streamlit as st


st.set_page_config(layout="wide")
about_page = st.Page(
    page="views/about_me.py",
    title="About Me",
    icon="🙎‍♂️",
    default=True,
)

project_1_page = st.Page(
    page="views/heart_disease_prediction/heart_disease_prediction.py",
    title="Heart Disease Prediction",
    icon="🫀",
)


pg = st.navigation(
    {
        "Info": [about_page],
        "Projects": [project_1_page] 
    }
)

st.sidebar.markdown("This dashboard created by : [Varel](https://www.linkedin.com/in/muhammadvarelantoni)")

pg.run()
