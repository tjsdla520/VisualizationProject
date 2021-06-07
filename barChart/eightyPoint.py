import pandas as pd
import matplotlib.pyplot as plt
################################################
#한글 깨짐 방지 설정
plt.rc('font', family='Malgun Gothic')
#저장파일 이름 설정
cnt, PNG, UNDERBAR = 0, '.png', '_'
CHART_NAME = 'EightyPoint'
#정보가 담긴 파일
filename = '../allleague.csv'
################################################
#파일 읽어오기
allleague = pd.read_csv(filename, encoding='utf-8', index_col='teamName')
#수치화할 컬럼 정하기
labels = allleague['gainPoint']
chardata = labels[labels > 80]
label_dict = {'FC 인터 밀란':'인터밀란','레알 마드리드 CF':'레얄마드리드','클루브 아틀레티코 데 마드리드':'아틀레티고데마드리드','파리 생제르맹 FC':'파리생제르맹','릴 OSC':'릴','맨체스터 시티 FC':'맨체스터시티'}
print(type(chardata))
plt.figure(figsize=(15,15))
colors = ['b','g','r','c','y','pink']
mycolor = colors[0:len(allleague)]
plt.rc('ytick', labelsize=15)
plt.rc('axes', titlesize=30)
plt.rc('xtick', labelsize=30)

chardata.plot( kind='barh',color=mycolor,xlabel='승점', ylabel='팀명', legend=False, title='유럽 5대 리그 20-21 승점 80 이상 팀', rot=11)

################################################
#반복되는 차트저장 형식을 저장하기
cnt += 1
savefilename = CHART_NAME + UNDERBAR + str(cnt).zfill(2) + PNG
plt.savefig(savefilename, dpi=400)
print(savefilename + ' 파일 저장 완료')
