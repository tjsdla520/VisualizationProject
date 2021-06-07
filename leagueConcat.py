import pandas as pd
from pandas import DataFrame
#######################################################################
myencoding = 'utf-8'
leagueList = ['epl', 'bundesliga', 'ligue1', 'primera', 'seria']
#######################################################################
newframe = DataFrame()
for oneleague in leagueList:
    filename = oneleague + '.csv'
    #.csv 파일을 모두 읽어오기
    myframe = pd.read_csv(filename, index_col=False, encoding=myencoding)
    #concat 함수 5개의 리그를 모두 합하기
    newframe = pd.concat([newframe, myframe], axis=0, ignore_index=True)
print(newframe.info())
########################################################################
#5대리그 20-21시즌 파일저장
totalfile = 'allleague.csv'
newframe.to_csv(totalfile, encoding=myencoding)
print(totalfile+'파일이 저장됨')