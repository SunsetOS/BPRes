import pandas as pd


data = pd.read_excel(r"./drop/01.xlsx")
data.to_csv("drop\\01.csv",index=False)