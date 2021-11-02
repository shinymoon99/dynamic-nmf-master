#to extract text according to time
import pandas as pd
import os
import jieba
from openpyxl import load_workbook
def makefile(path,content,filename):
    if os.path.exists(path):
        if os.path.isdir(path):
            f = open(path+"\\"+filename,'w+')
            f.write(content)
            f.seek(0)
            read = f.readline()
            f.close()
            print(read)
        else:
            print('please input the dir name')
    else:
        print('the path is not exists')

#aim to read data and save to different folder using dataframe
df = pd.read_excel(r"C:\Users\Happinessfuture\PycharmProjects\dynamic-nmf-master\data\cotton.xls")

#数据类型转换
df['Headline'] = df['Headline'].astype('str')

#实现数据的分词之后再读入
passagenum=df.shape[0]
stop= [line.strip() for line in
       open(r'C:\Users\Happinessfuture\PycharmProjects\dynamic-nmf-master\text\hit_stopwords.txt',encoding='utf-8-sig')]
mycut = lambda x: ' '.join(jieba.cut(x))
content=[]
tmp_cut = df['Headline'].apply(mycut)

#
content= tmp_cut.values.tolist()
#tmp_cut = tmp_cut.apply(lambda x: x.split(' '))
#tmp_cut = tmp_cut.apply(lambda x: [i for i in x if i not in stop])


dates=df['Date(Time)'].astype('datetime64[ns]')

for i in range(0,passagenum):
     makefile(r"C:\Users\Happinessfuture\PycharmProjects\dynamic-nmf-master\data\monthcotton"+"\\"+str(dates[i].month),str(df['Headline'][i]),str(i)+'.txt')
