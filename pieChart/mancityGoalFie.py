import pandas as pd
import matplotlib.pyplot as plt
################################################
#한글 깨짐 방지 설정
plt.rc('font', family='Malgun Gothic')
#저장파일 이름 설정
cnt, PNG, UNDERBAR = 0, '.png', '_'
CHART_NAME = 'mancityGoalFie'
#정보가 담긴 파일
filename = '../epl.csv'
################################################
#인덱스 기준설정 및 판다스로 파일 읽어오기
data = pd.read_csv(filename, index_col='teamName')
#맨체스터 시티의 아이템값을 저장
my_concern = [item for item in data.index if item in ['맨체스터 시티 FC']]
#변수명 기준으로 설정 / iloc = 인덱스번호로 설정
data = data.loc[my_concern]
print("data: ")
print(data)
#형변환후 1차원으로 저장
chartdata = [int(data['gainGoal']),int(data['loseGoal']),int(data['goalGap'])]

print('chardata : ')
print(chartdata)
mylabel = ['득점', '실점', '득실차']
mycolors = ['blanchedalmond', 'palegreen', 'pink']

plt.figure()
plt.pie(chartdata, labels=mylabel, shadow=False, explode=(0, 0.05, 0),
        colors=mycolors, autopct='%1.2f%%', startangle=90, counterclock=False)

plt.grid(True)
plt.legend(loc=3)
plt.legend(loc='upper right')
plt.xlabel('20-21 시즌 득점,실점,득실차')
plt.title('맨체스터시티 20-21 시즌 득점,실점,득실차 비율 그래프')
plt.rcParams['font.size'] = 18
################################################
#반복되는 차트저장 형식을 저장하기
cnt += 1
savefilename = CHART_NAME + UNDERBAR + str(cnt).zfill(2) + PNG
plt.savefig(savefilename, dpi=400)
print(savefilename + ' 파일 저장 완료')
