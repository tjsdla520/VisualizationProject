import time
import pandas as pd

from selenium import webdriver
from bs4 import BeautifulSoup

class leagueinfo():
    #파일 저장
    def saveCsv(self, result):
        mycolumn = ['leaguename','rank', 'teamName', 'gameCount', 'gainPoint', 'won', 'drawn', 'lost', 'gainGoal', 'loseGoal', 'goalGap']
        #판다스로 csv파일로 저장하기
        data = pd.DataFrame(result, columns=mycolumn)
        data.to_csv(self.leagueName + '.csv', encoding='utf-8', index=False)
        print(self.leagueName + '파일 생성 완료')

    #생성자 생성
    def __init__(self, leagueName, url):
        self.leagueName = leagueName
        self.url = url
        filepath = 'd:/chromedriver.exe'
        self.driver = webdriver.Chrome(filepath)
        self.driver.get(self.url)

    #셀리니움으로 웹페이지 크롤링
    def getWebDriver(self):
        wait = 3
        time.sleep(wait)
        #소스보기
        mypage = self.driver.page_source
        #BeautifulSoup 객체 리턴턴
        return BeautifulSoup(mypage, 'html.parser')