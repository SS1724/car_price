import streamlit as st
import pandas as pd
import pickle

# Load the trained model
model = pickle.load(open('model.pkl', 'rb'))

# Streamlit app title
st.title('Car Price Prediction App')

# Sidebar with input fields
st.sidebar.header('Input Features')

year = st.sidebar.slider('Year', 2000, 2023, 2015)
present_price = st.sidebar.number_input('Present Price (in lakhs)', min_value=0.1, max_value=100.0, value=5.0)
kms_driven = st.sidebar.number_input('Kms Driven', min_value=1, max_value=1000000, value=50000)
owner = st.sidebar.selectbox('Owner', [0, 1, 2, 3])

fuel_type = st.sidebar.radio('Fuel Type', ['Petrol', 'Diesel'])
if fuel_type == 'Petrol':
    fuel_type_diesel = 0
    fuel_type_petrol = 1
else:
    fuel_type_diesel = 1
    fuel_type_petrol = 0

seller_type = st.sidebar.radio('Seller Type', ['Dealer', 'Individual'])
if seller_type == 'Dealer':
    seller_type_individual = 0
else:
    seller_type_individual = 1

transmission = st.sidebar.radio('Transmission', ['Manual', 'Automatic'])
if transmission == 'Manual':
    transmission_manual = 1
else:
    transmission_manual = 0

# Create a DataFrame from user input
user_input = pd.DataFrame({
    'Year': [year],
    'Present_Price': [present_price],
    'Kms_Driven': [kms_driven],
    'Owner': [owner],
    'Fuel_Type_Diesel': [fuel_type_diesel],
    'Fuel_Type_Petrol': [fuel_type_petrol],
    'Seller_Type_Individual': [seller_type_individual],
    'Transmission_Manual': [transmission_manual]
})

# Make predictions
if st.sidebar.button('Predict'):
    predicted_price = model.predict(user_input)
    st.subheader('Predicted Selling Price')
    st.write(f'₹{predicted_price[0]:,.2f} lakhs')
