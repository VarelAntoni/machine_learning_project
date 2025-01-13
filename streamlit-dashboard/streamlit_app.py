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

project_2_page = st.Page(
    page="views/movies_dataset/movies_dataset.py",
    title="Movies dataset",
    icon="🎬",
)


pg = st.navigation(
    {
        "Info": [about_page],
        "Projects": [project_1_page, project_2_page] 
    }
)

st.sidebar.markdown("This dashboard created by : [Varel](www.linkedin.com/in/muhammadvarelantoni)")
st.sidebar.markdown("linkedin : [Muhammad Varel Antoni](www.linkedin.com/in/muhammadvarelantoni)")
st.sidebar.markdown("GitHub : [VarelAntoni](https://github.com/VarelAntoni)")


pg.run()