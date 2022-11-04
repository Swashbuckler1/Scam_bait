import pandas as pd
from sdv.tabular import GaussianCopula

df = pd.read_csv("Finance_data.csv")
model = GaussianCopula()
model.fit(df)

new_data = model.sample(num_rows=20)
new_data.to_csv("Financials.csv", index=False)
