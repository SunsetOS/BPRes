import pandas as pd
import csv
def ConverFile():
    for i in range(1,11):
        data = pd.read_excel(f'./notdrop/{i:0>2d}.xlsx')
        data.to_csv(f'./output/notdrop/{i:0>2d}.csv', index=False)
        print("File", i, "is converted to csv")

def ModifyCSV():
    for i in range(1,11):
        with open(f'./output/notdrop/{i:0>2d}.csv', 'r') as f:
            reader = csv.reader(f)
            data = list(reader)
            data.pop(0)

            for j in data:
                j.pop(0)
                j.pop(0)
                j.pop(0)
            with open(f'./output/noheader/notdrop/{i:0>2d}.csv', 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerows(data)
            print("File", i, "is save to csv")

ModifyCSV()