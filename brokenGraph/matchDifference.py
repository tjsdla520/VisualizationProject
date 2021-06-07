import pandas as pd
import matplotlib.pyplot as plt
################################################
#한글 깨짐 방지 설정
plt.rc('font', family='Malgun Gothic')
#저장파일 이름 설정
cnt, PNG, UNDERBAR = 0, '.png', '_'
CHART_NAME = 'matchDifference'
#정보가 담긴 파일
filename = '../allleague.csv'
################################################
#########승과 패를 이중축으로 그리기########################
#판다스로 파일 읽어오기
myframe = pd.read_csv(filename)
print(type(myframe))
print(myframe.columns)
print('-'*40)
#슬라이싱
data_won = myframe.loc[:, ['won']]
data_lost = myframe.loc[:, ['lost']]
#동시에 데이터 그리기
fig, ax1 = plt.subplots()
ax1.set_title('5대리그 전체팀 승패(이중 축) ')
#x축 행수 구하기
xrange = range(len(myframe))
color = 'tab:red'
ax1.set_xlabel('전체 팀의 수')
ax1.set_ylabel('승', color=color)
data1=ax1.plot(xrange, data_won, color=color,linestyle='-.',label='각 팀별 승', marker='o',markersize=4)
ax1.tick_params(axis='y', labelcolor=color)
#동일한 x축을 기준으로하는 다른 y축생성
ax2 = ax1.twinx()
color = 'tab:blue'
ax2.set_ylabel('패', color=color)
data2=ax2.plot(xrange, data_lost, color=color,linestyle='--',label='각 팀별 패', marker='s',markersize=4)
ax2.tick_params(axis='y', labelcolor=color)
#범례 설정
legenddadta = data1 + data2
labels = [l.get_label() for l in legenddadta]
plt.legend(legenddadta, labels, loc=1)
# #레이아웃에 맞게끔 조절
fig.tight_layout()

################################################
#반복되는 차트저장 형식을 저장하기
cnt += 1
savefilename = CHART_NAME + UNDERBAR + str(cnt).zfill(2) + PNG
plt.savefig(savefilename, dpi=400)
print(savefilename + ' 파일 저장 완료')
