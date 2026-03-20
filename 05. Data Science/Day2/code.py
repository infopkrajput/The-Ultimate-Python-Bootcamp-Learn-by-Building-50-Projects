import numpy as np
import pandas as pd

np.random.seed(42)

years = np.random.uniform(0.5, 10, 100).round(2)

salary = (years * 5000 + np.random.normal(0, 10000, 100)).round(2)

data = pd.DataFrame({"Years of Experience": years, "Salary": salary})

data.to_csv("data.csv", index=False)
print(f"Data saved to data.csv")

