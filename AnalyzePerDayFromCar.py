"""
需求：统计每天的数据，写成txt文件

"""
import pandas as pd
import numpy as np

def getSeri(day):
    df=pd.read_csv("F:\\BWMProject\\taxi data\\"+day+".csv")
    cor=df.coordinates
    return df,cor


"""
@param 文件字符串
"""
def wirteTxtFile(dayString):
    newdf=pd.DataFrame()
    df,cor=getSeri(dayString)
    numList=[]
    for key,value in cor.items():
        strList=value.split(",")
        numList.append(int(len(strList)/2))
    newdf['datetime']=df['datetime']
    newdf["num"]=numList
    newdf.to_csv("F:\\BWMProject\\11.12\\"+dayString+".txt",index=False,sep='\t')



if __name__=="__main__":
    for i in range(1,31):
        daystr="2018-09-0%d"%i if i<10 else "2018-09-%d"%i
        wirteTxtFile(daystr)

