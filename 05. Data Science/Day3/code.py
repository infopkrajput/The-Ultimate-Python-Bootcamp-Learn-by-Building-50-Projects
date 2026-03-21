import pandas as pd 
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data = pd.read_csv('data.csv')

x = data[["Years of Experience"]]
y = data[["Salary"]]

model = LinearRegression()
model.fit(x.values.reshape(-1, 1), y)

data['Predicted Salary'] = model.predict(x.values.reshape(-1, 1))

print("Model Coefficient (slope)", round(float(model.coef_[0][0]), 2))
print("Model Intercept (base salary)", round(float(model.intercept_[0]), 2))

plt.scatter(x, y, color='blue',label='Actual Salary')
plt.plot(x, data['Predicted Salary'], color='red', label='Regression Line')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.title('Linear Regression')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()