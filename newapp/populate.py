import pandas as pd
location= 'D:\University\CSE 303 (Database)\Project\Datasets\classSize_1.xlsx'
files= pd.read_excel(location)
toRead= files['COFFER_COURSE_ID'].values.tolist()
count=0
while (count<len(toRead)):
    print(toRead[count])
    count=count+1