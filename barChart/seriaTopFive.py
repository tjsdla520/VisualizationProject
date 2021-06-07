import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
################################################
#한글 깨짐 방지 설정
plt.rc('font', family='Malgun Gothic')
#저장파일 이름 설정
cnt, PNG, UNDERBAR = 0, '.png', '_'
CHART_NAME = 'seriaTopFive'
#정보가 담긴 파일
filename = '../seria.csv'
################################################
#팀이름을 기준으로 판다스로 파일 읽어오기
data = pd.read_csv(filename, index_col='teamName')
TEAM = ['FC 인터 밀란','AC 밀란','아탈란타 BC','유벤투스 FC','SSC 나폴리']
WHEN = ['gainGoal', 'loseGoal', 'goalGap']
data = data.loc[TEAM, WHEN]
print(data)
data.index.name = '팀명'
plt.figure()
stacked=False
yticks_interval = 5
data.plot(kind='bar', rot=10, title='seria top 5 골득실차', legend=True, stacked=stacked)
# plt.legend(loc=label_dict)
if stacked == False:
    maxlim = (int(max(data.max()) / yticks_interval) + 1) * yticks_interval
    print('maxlim : ', maxlim)
    values = np.arange(0, maxlim + 1, yticks_interval)
    plt.yticks(values, ['%s' % format(val, ',') for val in values])
else : # 누적 막대 그래프
    # 누적 합인 data.sum(axis=1))의 최대 값에 대한 연산이 이루어 져야 합니다.
    maxlim = (int(max(chartdata.sum(axis=1)) / yticks_interval) + 1) * yticks_interval
    print('maxlim : ', maxlim)
    values = np.arange(0, maxlim + 1, yticks_interval)
    plt.yticks(values, ['%s' % format(val, ',') for val in values])
# y축의 상하한 값이 주어 지는 경우에만 설정합니다.
    if ylim != None :
        plt.ylim(ylim)
################################################
#반복되는 차트저장 형식을 저장하기
cnt += 1
savefilename = CHART_NAME + UNDERBAR + str(cnt).zfill(2) + PNG
plt.savefig(savefilename, dpi=400)
print(savefilename + ' 파일 저장 완료')

