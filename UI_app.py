import pandas as pd
import streamlit as st
import joblib

Model = joblib.load("credit_card_fraud_detection_model.pkl")
Scaling = joblib.load("scaler.pkl")

st.set_page_config(page_title = "Credit Card Fraud Detection System", 
                   layout = "centered")

st.markdown("<h1 style = 'text-align: center;'> Credit Card Fraud Detection System</h1>",
            unsafe_allow_html = True)


The_file = st.file_uploader("The CSV file should be upload here", type = ["csv"])

if The_file is not None:
    try:
        Input_data = pd.read_csv(The_file)

        col = [f"V{i}" for i in range(1, 29)] + ["Amount"]

        if list(Input_data.columns) != col:
            st.error(f"Input V1 to V28 and Amount must be there in CSV file")

        else:
            st.success("The file is uploaded effortlessly")

            Index_row = st.number_input("Choose the row index", min_value = 1, max_value = len(Input_data), step = 1)

            if st.button("Predict"):
                row_input = Input_data.iloc[[Index_row - 1]]

                output_result = Model.predict(row_input)[0]

                if output_result == 0:
                    label = "It is a Legitimate Transaction."
                else:
                    label = "It is a Fraudulent Transaction." 

                
                st.subheader("Show the choosen row data")
                st.write(row_input)

                st.subheader("The prediction is: ")
                st.success(f"Prediction: {label}")

    except Exception as e:
        st.error(f"Unexpected error: {e}")

