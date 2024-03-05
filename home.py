import streamlit as st
from PIL import Image

def home():

    image = Image.open("diabetes.png")

    # Display the image in your Streamlit app
    st.image(image, use_column_width=True)

    # Introduction
    st.header("Welcome to the Diabetes Prediction App!")
    st.write('''Embark on a journey to predict the likelihood of diabetes based on various
    health indicators. This web app showcases the power of machine learning in predicting
    health outcomes.''')

    # Key Features
    st.subheader("Key Features:")
    st.write('''1. Predictive Analytics:
    Explore the predictions of diabetes risk using advanced analytics. The model considers
    features such as pregnancies, glucose levels, blood pressure, skin thickness, insulin
    levels, BMI, diabetes pedigree function, and age.''')

    st.write('''2. User-Friendly Interface:
    Navigate through the app effortlessly. No expertise required – simply input health
    indicators and witness the predictive magic.''')

    st.write('''3. Data Visualization:
    Visualize patterns and trends in the dataset with interactive charts. Gain insights into the
    factors influencing diabetes risk.''')

    # About the Project
    st.subheader("About the Project:")
    st.write('''The Diabetes Prediction project combines historical data with modern data
    science techniques. Join us in exploring the features that play a role in determining
    diabetes risk.''')

    # About Me
    st.subheader("About Me:")
    st.write('''Curious about the mind behind the predictions? I'm SRIKHANTH, a dedicated
    data analyst certified by Google passionate about unraveling insights from data.''')

    st.write('''Feel free to connect with me on [LinkedIn](https://www.linkedin.com/in/srikhanth-r) or explore more
    projects on my [portfolio](https://www.datascienceportfol.io/srikhanth_r). Let's dive deep into the world of data science
    together!''')

    # Call to Action
    st.write('''Ready to embark on this predictive journey? Head over to the Input form page to
    input health indicators and make your own diabetes risk predictions!''')


