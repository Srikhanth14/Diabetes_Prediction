import streamlit as st
import pandas as pd

def dataset():

    # Dataset Information
    st.header("Dataset Information:")
    st.write('''The predictive model is trained on a dataset containing information about diabetes
    patients, including features such as pregnancies, glucose levels, blood pressure, skin thickness,
    insulin levels, BMI, diabetes pedigree function, and age.''')

    # Data Source
    st.header("Data Source:")
    st.write("For more details, you can explore the dataset on Kaggle: [Click Here](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database)")

    # Sample Data
    st.header("Sample Data:")
    st.write("Here's a glimpse of the diabetes dataset:")
    data = pd.read_csv("diabetes.csv") 
    st.dataframe(data.head())

    st.subheader("Download Dataset")
    st.write("You can download the full diabetes dataset for further exploration:")
    def data_read(data):
        return data.to_csv().encode('utf-8')
    csv=data_read(data)

    st.download_button(
                        label='Download Sample Data',
                        data=csv,
                        file_name='diabetes.csv',
                        mime='text/csv'      
                    )

    # Input Your Data
    st.header("Input Your Data:")
    st.write('''Want predictions for your specific patient details? Enter your data in the input
    form and discover the forecasted diabetes risk outcome.''')

    # Guidance on Data Format
    st.header("Guidance on Data Format:")
    st.write('''To ensure successful predictions, enter your data with the same features as the
    sample data. Include columns for pregnancies, glucose levels, blood pressure, skin thickness,
    insulin levels, BMI, diabetes pedigree function, and age.''')

    # GitHub Link
    st.header("GitHub Repository:")
    st.write("Explore the code and details of this project on my GitHub repository:")
    st.write("[Diabetes Prediction GitHub Repository](https://github.com/Srikhanth14/Diabetes_Prediction)")

    # Conclusion
    st.write('''Ready to get predictions for your data? Input your patient details in the input
    form, and let the Diabetes Prediction app work its magic!''')
