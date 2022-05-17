import pandas as pd

# df_excel = pd.read_excel(r"C:\Prashanti M\data1.xlsx")
# print(df_excel)
#
# df_csv = pd.read_csv(r"C:\Prashanti M\dept.csv")
# print(df_csv)


info = {
    'name' : ['earth','sky','fah','fire','air'],
    'occupation' : ['HR','Actor','Cook ','CEO','Army'],
    'salary' : [102000,202221,342212,452311,111098]
}
index_no = [101,102,103,104,105]
df_info=pd.DataFrame(data=info)
df_csv =pd.read_csv(r"C:\Prashanti M\dept.csv")
df_info.to_csv(r"C:\Prashanti M\sampledf.csv")
print(df_csv)
print(df_info.columns)
print(df_info.dtypes)
