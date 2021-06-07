import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
########################################################################
plt.rc('font', family='Malgun Gothic')
cnt, PNG, UNDERBAR = 0, '.png', '_'
CHART_NAME = 'histogram'
filename = '../allleague.csv'
########################################################################
################################################
#############3개의 차트를 동시에 그리기########
data = pd.read_csv(filename, encoding='utf-8')
fig, axes = plt.subplots(nrows=1, ncols=3)
won = data['won']
drawn = data['drawn']
lost = data['lost']

axes[0].hist(won, range=(1, 30), bins=10, alpha=0.6, color='magenta')
axes[1].hist(drawn, range=(1, 30), bins=10, alpha=0.6, color='aqua')
axes[2].hist(lost, range=(1, 30), bins=10, alpha=0.6, color='greenyellow')
axes[0].set_title('20-21시즌 승리 수')
axes[1].set_title('20-21시즌 무승수')
axes[2].set_title('20-21시즌 패배 수')

#############반복되는 차트저장 형식을 저장하기########
cnt += 1
savefilename = CHART_NAME + UNDERBAR + str(cnt).zfill(2) + PNG
plt.savefig(savefilename, dpi=400)
print(savefilename + ' 파일 저장 완료')

##############################################################
####한 차트에 모아서 그리기#######################################

fig, axes = plt.subplots()
axes.hist(won, bins=10, alpha=0.6)
axes.hist(drawn, bins=10, alpha=0.6)
axes.hist(lost, bins=10, alpha=0.6)
axes.set_title('유럽 5대리그 승,무,패 모두 나타낸 하나의 히스토그램')
##############################################################

cnt += 1
savefilename = CHART_NAME + UNDERBAR + str(cnt).zfill(2) + PNG
plt.savefig(savefilename, dpi=400)
print(savefilename + ' 파일 저장 완료')

##############################################################
##승,무,패 누적 히스토그램으로 그리기#########################################
fig, axes = plt.subplots()
won = data['won']
drawn = data['drawn']
lost = data['lost']
x = np.array([won,drawn,lost]).T
axes.hist(x, bins=10, density=False, histtype='bar', stacked=True)
axes.set_title('유럽 5대리그 승,무,패 누적 히스토그램')
##############################################################

cnt += 1
savefilename = CHART_NAME + UNDERBAR + str(cnt).zfill(2) + PNG
plt.savefig(savefilename, dpi=400)
print(savefilename + ' 파일 저장 완료')

