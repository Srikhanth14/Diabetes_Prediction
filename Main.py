import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
import home,Dataset,Visualization,Input

st.set_page_config(page_title="Diabetes Prediction", page_icon="heartbeat", layout="wide")  

selected = option_menu(
    menu_title="Diabetes Prediction",
    options=["Home", "Dataset", "Visualization", "Input_form"],
    icons=["house-fill", "database-down", "pie-chart", "ui-radios-grid"],
    menu_icon="heart-pulse",
    default_index=0,
    orientation="horizontal"
)

if selected == "Home":
    home.home()
elif selected == "Dataset":
    Dataset.dataset()
elif selected == "Visualization":
    # Load the diabetes dataset
    uploaded_file = st.file_uploader("Upload a file", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        # Call the visualization function
        Visualization.visualization(df)
elif selected == "Input_form":
    Input.app()

