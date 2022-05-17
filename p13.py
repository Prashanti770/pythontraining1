#pandas library

import  pandas as pd

info = {
    'name' : ['earth','sky','fah','fire','air'],
    'occupation' : ['HR','Actor','Cook ','CEO','Army'],
    'salary' : [102000,202221,342212,452311,111098]
}
index_no = [101,102,103,104,105]
# df=pd.DataFrame(data=info)
# print(df) #prints df in tabular format with default index starts from 0

df =pd.DataFrame(data=info,index=index_no)
print(df)

print(df.size)
print(df.shape)

print(df.head(3))
print(df.tail(2))
names = df.loc[103]
print(names)
