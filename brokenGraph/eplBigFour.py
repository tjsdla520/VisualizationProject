import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
################################################
#한글 깨짐 방지 설정
plt.rc('font', family='Malgun Gothic')
#저장파일 이름 설정
cnt, PNG, UNDERBAR = 0, '.png', '_'
CHART_NAME = 'eplBigFour'
#정보가 담긴 파일
filename = '../eplTen.csv'
################################################
#판다스로 파일 읽어오기
df = pd.read_csv(filename)
#피봇테이블로 행과 열을 변경
pivot = df.pivot_table(values='rank', index='teamName', columns='leaguename')
print(pivot.columns)
print(pivot)
#epl리그 big 4 team 선정
TEAM = ['첼시 FC', '맨체스터 유나이티드 FC', '맨체스터 시티 FC', '리버풀 FC']
WHEN = [ 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
chartdata = pivot.loc[TEAM, WHEN]
print('-' * 30)
print(type(chartdata))
#x축, y축 반전
chartdata=chartdata.T
chartdata.plot(title='09~21 시즌 epl big 4 순위', figsize=(10, 6), legend = True, marker='o', rot=10)
plt.xlabel('시즌')
plt.ylabel('순위')
plt.gca().invert_yaxis()
################################################
#반복되는 차트저장 형식을 저장하기
cnt += 1
savefilename = CHART_NAME + UNDERBAR + str(cnt).zfill(2) + PNG
plt.savefig(savefilename, dpi=400)
print(savefilename + ' 파일 저장 완료')