import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
################################################
#한글 깨짐 방지 설정
plt.rc('font', family='Malgun Gothic')
#저장파일 이름 설정
cnt, PNG, UNDERBAR = 0, '.png', '_'
CHART_NAME = 'mancityWonFie'
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
chartdata = [int(data['won']),int(data['drawn']),int(data['lost'])]
print('-'*90)

print(chartdata)
#서브플롯 객체생성 / 사용할 키워드 담는 dict
fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

def getLabelFormat(pct, allvals):
    absolute = int(pct/100.*np.sum(allvals))
    return "{:.2f}%\n({:d} 건)".format(pct, absolute)
mylabel = ['승리', '무승부', '패배']

wedges, texts, autotexts = ax.pie(chartdata,labels=mylabel ,autopct=lambda pct: getLabelFormat(pct, chartdata), textprops=dict(color="w"))
ax.legend(loc=3)
ax.legend(loc='upper right',prop={'size': 8})

#선 두께 조절
plt.setp(autotexts, size=8, weight="bold")
ax.set_title("맨체스터시티 20-21 시즌 승,무,패 비율 그래프")

################################################
#반복되는 차트저장 형식을 저장하기
cnt += 1
savefilename = CHART_NAME + UNDERBAR + str(cnt).zfill(2) + PNG
plt.savefig(savefilename, dpi=400)
print(savefilename + ' 파일 저장 완료')

