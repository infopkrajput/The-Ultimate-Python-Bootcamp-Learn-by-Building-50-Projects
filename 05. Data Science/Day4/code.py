import pandas as pd 
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import streamlit as st 

data = pd.read_csv('data.csv')

x = data[["Years of Experience"]]
y = data[["Salary"]]

model = LinearRegression()
model.fit(x, y)

st.title("Salary Prediction based on Years of Experience")
st.write("Enter the number of years of experience to predict the salary:")

years_of_experience = st.number_input("Years of Experience", min_value=0.0, max_value=50.0, step=0.1)

if years_of_experience:
    print(years_of_experience)
    
    predicted_salary = model.predict([[years_of_experience]])[0]
    st.success(f"Estimated Salary : {predicted_salary}")
    
st.subheader("Regression data.")

fig, ax = plt.subplots()
ax.scatter(x, y, color='blue',label='Actual Salary')
ax.plot(x, model.predict(x), color='red', label='Regression Line')
ax.set_xlabel('Years of Experience')
ax.set_ylabel('Salary')
ax.set_title('Linear Regression')
ax.legend()
st.pyplot(fig)
