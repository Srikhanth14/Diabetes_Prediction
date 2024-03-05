import streamlit as st
import pandas as pd
import numpy as np
import pickle


def app():
    loaded_model = pickle.load(open("Diabetes_Model.sav","rb"))

    # Creating function for prediction
    def diabetics_prediction(input_data):

        # Change the input data to a numpy array
        input_data_np_array = np.asarray(input_data)

        # Reshape the numpy array as we are predicting for only one instance
        input_data_reshaped = input_data_np_array.reshape(1, -1)
        column_names = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']
        # Make predictions using the trained model
        input_data_reshaped_df = pd.DataFrame(input_data_reshaped,columns=column_names)
        prediction = loaded_model.predict(input_data_reshaped_df)

        # Display prediction result
        if prediction[0] == 0:
            st.error("The person is not diabetic.")
        else:
            st.success("The person is diabetic.")

    def main():
        st.title('Diabetics Prediction Web App')
        st.write("Enter the Patient Details: ")
        Pregnancies = st.text_input("Number of Pregnancies")
        Glucose = st.text_input('Glucose Level')
        BloodPressure = st.text_input('Blood Pressure')
        SkinThickness = st.text_input('Skin Thickness')
        Insulin = st.text_input('Insulin Level')
        BMI = st.text_input('BMI')
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function')
        Age = st.text_input('Age')

        if st.button('Diabetics Test Result'):
                diabetics_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])


    main()
