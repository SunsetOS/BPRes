import pandas as pd
import csv
def ConverFile():
    for i in range(1,11):
        data = pd.read_excel(f'./PreProcess/notdrop/{i:0>2d}.xlsx')
        data.to_csv(f'./PreProcess/output/notdrop/{i:0>2d}.csv', index=False)
        print("File", i, "is converted to csv")

def ModifyCSV():
    for i in range(1,11):
        with open(f'./PostProcess/output/notdrop/{i:0>2d}.csv', 'r') as f:
            reader = csv.reader(f)
            data = list(reader)
            data.pop(0)

            for j in data:
                j.pop(0)
                j.pop(0)
                j.pop(0)
            with open(f'./PostProcess/noheader/notdrop/{i:0>2d}.csv', 'w', newline = '') as f:
                writer = csv.writer(f)
                writer.writerows(data)
            print("File", i, "save to csv")

def Mark():
    for i in range(1,11):
        with open(f'./PostProcess/noheader/notdrop/{i:0>2d}.csv', 'r') as f:
            reader = csv.reader(f)
            data = list(reader)
            for j in data:
                j.append('0')
            with open(f'./PostProcess/noheader/notdrop/{i:0>2d}.csv', 'w', newline = "") as f:
                writer = csv.writer(f)
                writer.writerows(data)
            print("File", i, "is tagged")
    for i in range(1,11):
        with open(f'./PostProcess/noheader/drop/{i:0>2d}.csv', 'r') as f:
            reader = csv.reader(f)
            data = list(reader)
            for j in data:
                j.append('1')
            with open(f'./PostProcess/noheader/drop/{i:0>2d}.csv', 'w', newline = "") as f:
                writer = csv.writer(f)
                writer.writerows(data)
            print("File", i, "is tagged")

ModifyCSV()