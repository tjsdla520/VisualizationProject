import pandas as pd

import pandas as pd
import matplotlib.pyplot as plt
############################################################################################################
plt.rc('font', family='Malgun Gothic')
cnt, PNG, UNDERBAR = 0, '.png', '_'
CHART_NAME = 'scatterLeague'
filename = '../allleague.csv'
############################################################################################################
data = pd.read_csv(filename, encoding='utf-8')
#유니크값으로 추출
labels = data['leaguename'].unique()
#사전으로 저장
label_dict = {'epl':'프리미어리그','bundesliga':'분데스리가','ligue1':'리그앙','primera':'프리메라리가','seria':'라리가'}
mycolors=['c','g','b','m','r']
#색지정을 위한 임의의 변수 선언
idx=0
plt.figure()

for finditem in labels:
    #x축, y축 값 기준 설정
    xdata = data.loc[data['leaguename'] == finditem, 'gainPoint']
    ydata = data.loc[data['leaguename'] == finditem, 'gainGoal']
    plt.plot(xdata, ydata, color=mycolors[idx], marker='o', linestyle='None', label=label_dict[finditem])
    idx += 1

plt.legend()
plt.xlabel("승점")
plt.ylabel("득점")
plt.title("20-21시즌 유럽 5대리그 승점, 득점 산점도 그래프")
plt.grid(True)
################################################
#반복되는 차트저장 형식을 저장하기
cnt += 1
savefilename = CHART_NAME + UNDERBAR + str(cnt).zfill(2) + PNG
plt.savefig(savefilename, dpi=400)
print(savefilename + ' 파일 저장 완료')