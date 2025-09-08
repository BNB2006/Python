import pandas as pd

data1 = {
    "ID" : [1, 2, 3, 4],
    "Name" : [ 'Alice','Bob', 'Charli', 'David'],
    "Department" : ['HR', 'IT', 'Finance', 'HR']
}

df_data1 = pd.DataFrame(data1)
print(df_data1)
print()

data2 = {
    "ID" : [1, 3, 5, 6],
    "Salary" : [60000, 75000, 80000, 55000],
    "Year Experiance" : [5, 8, 3, 2]
}

df_data2 = pd.DataFrame(data2)
print(df_data2)
print()

df_merge_inner = pd.merge(df_data1, df_data2, how='inner', on = 'ID')
print(df_merge_inner)
print()

df_merge_outer = pd.merge(df_data1,df_data2, how = 'outer',on = 'ID')
print(df_merge_outer)
print()

df_merge_left = pd.merge(df_data1, df_data2, how='left', on = 'ID')
print(df_merge_left)
print()

df_merge_right = pd.merge(df_data1,df_data2, how = 'right',on = 'ID')
print(df_merge_right)
print()

df_merge = pd.merge()
print(df_merge)
print()
