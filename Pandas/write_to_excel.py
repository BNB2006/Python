import pandas as pd

data = {
    'Name': ['RamLal', 'ShamLal', 'GhanSham'],
    'Age': [25, 30, 35]
}
data1 = {
    'Name': ['RAju', 'CHUTKI', 'JAGGU'],
    'Age': [25, 30, 35]
}

df = pd.DataFrame(data)
dp = pd.DataFrame(data1)

writer = pd.ExcelWriter('demo_excel.xlsx', engine='openpyxl')

df.to_excel(writer, sheet_name='Sheet1', index=False)
dp.to_excel(writer, sheet_name='Sheet2', index=False)

print("Data written to Excel file successfully!")
