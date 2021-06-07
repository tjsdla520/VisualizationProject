import re
import pandas.util
from Soccerutil import leagueinfo
from itertools import count
##############################################################################################################
leagueName = 'seria'#리그이름
base_url = 'https://sports.news.naver.com/wfootball/record/index.nhn' #접속 url
##############################################################################################################
def getData():
    saveData = []
    url = base_url
    url += '?category=%s' % str(leagueName)
    url += '&year=2020&tab=team'
    print('페이지가 호출됨')

    #Soccerutil.py의 클래스 호출
    serialeague = leagueinfo(leagueName, url)
    # 셀리니움으로 웹페이지 크롤링
    soup = serialeague.getWebDriver()
    league_list = soup.select_one('tbody')
    mytrlists = league_list.find_all('tr')

    for mytd in mytrlists:
        mytrlists = mytd.findAll('td')

        if (len(mytrlists)) > 1:
            rank = mytd.select_one('td:nth-of-type(1)').div.strong.string
            print(rank)
            teamName = mytd.select_one('td:nth-of-type(2)').div.span.string
            print(teamName)
            gameCount = mytd.select_one('td:nth-of-type(3)').div.span.string
            print(gameCount)
            gainPoint = mytd.select_one('td:nth-of-type(4)').div.span.string
            print(gainPoint)
            won = mytd.select_one('td:nth-of-type(5)').div.span.string
            print(won)
            drawn = mytd.select_one('td:nth-of-type(6)').div.span.string
            print(drawn)
            lost = mytd.select_one('td:nth-of-type(7)').div.span.string
            print(lost)
            gainGoal = mytd.select_one('td:nth-of-type(8)').div.span.string
            print(gainGoal)
            loseGoal = mytd.select_one('td:nth-of-type(9)').div.span.string
            print(loseGoal)
            goalGap = mytd.select_one('td:nth-of-type(10)').div.span.string
            print(goalGap)
            saveData.append(
                [leagueName, rank, teamName, gameCount, gainPoint, won, drawn, lost, gainGoal, loseGoal, goalGap])

    # seria리그 크롤링 결과물 저장
    serialeague.saveCsv(saveData)


##############################################################################################################
print(leagueName + '크롤링 시작')
getData()
print(leagueName + '크롤링 끝')