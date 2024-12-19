import pandas as pd

def ReadFile():
    for i in range(1,11):
        data = pd.read_excel(f'./notdrop/{i:0>2d}.xlsx')
        data.to_csv(f'./output/notdrop/{i:0>2d}.csv', index=False)
        print("File", i, "is converted to csv")
