# -*- coding: utf-8 -*-
import folium
import requests
import pandas as pd
#######################################################
#kakao developers사용
url_header = 'https://dapi.kakao.com/v2/local/search/address.json?query='
api_key = 'c48e791b1e21b66bb2d8a5bd073cf436'
header = {'Authorization': 'KakaoAK ' + api_key}
#################################################################
def getGocoder(address):
    result = ''
    url = url_header+address
    r = requests.get(url,headers=header)
    # http 응답코드 200 = okay
    if r.status_code ==200:
        try:
            #json = 키, 값 구조로 표현하는 표현기법
            result_address = r.json()["documents"][0]["address"]
            result = result_address["y"], result_address["x"]
        except Exception as err:
            return None
    else :
        result = "ERROR[" + str(r.status_code)+"]"
    return result
# end def getGocoder(address):


def makeMap(stadium, geoInfo):
    #경기장 이름 수정후 리스트으로 저장
    stadiuminfo = stadium_dict[stadium]
    #맵에서 나탈 색을 리스트로 저장
    mycolor = stadium_color[stadium]
    latitude, longitude = float(geoInfo[0]), float(geoInfo[1])

    #마커 그리기
    folium.Marker([latitude, longitude], popup=stadiuminfo, icon=folium.Icon(color=mycolor, icon='info-sign')).add_to(mapObject)
#end def makeMap(brand, store, geoInfo):

stadium_dict = {'서울월드컵경기장':'서울월드컵경기장','수원월드컵경기장':'수원월드컵경기장','대전월드컵경기장':'대전월드컵경기장','인천문학경기장':'인천월드컵경기장','울산문수축구경기장':'울산월드컵경기장','전주월드컵경기장':'전주월드컵경기장','광주월드컵경기장':'광주월드컵경기장','제주월드컵경기장':'제주월드컵경기장','대구스타디움':'대구월드컵경기장','부산아시아드주경기장':'부산월드컵경기장'}
stadium_color = {'서울월드컵경기장':'lightblue','수원월드컵경기장':'lightgreen','대전월드컵경기장':'darkpurple','인천문학경기장':'lightgray','울산문수축구경기장':'red','전주월드컵경기장':'green','광주월드컵경기장':'darkblue','제주월드컵경기장':'orange','대구스타디움':'gray','부산아시아드주경기장':'pink'}

# 지도의 기준점
mylatitude = 35.194012
mylongitude = 128.101959
#포리움으로 맵 그리기
mapObject = folium.Map(location=[mylatitude, mylongitude], zoom_start=7)
#파일 읽어오기
csv_file = 'worldcup.csv'
myframe = pd.read_csv(csv_file, index_col=0, encoding='utf-8')
print(myframe)

ok, notok = 0,0
#지도 그리기
for idx in range(len(myframe.index)):
    #지도에 필요한 경기장 이름과 주소 추출
    stadium = myframe.iloc[idx]['stadium']
    address = myframe.iloc[idx]['address']
    geoInfo = getGocoder(address)
    print(stadium)
    print(geoInfo)

    if geoInfo == None:
        print('notok :'+address)
        notok +=1
    else :
        print('ok :' + stadium + ' ' +address)
        ok += 1
        #ok가 되어야만 지도를 그린다
        makeMap(stadium, geoInfo)

total = ok +notok
filename = 'c:/imsi/worldcupStadium.html'
mapObject.save(filename)
print('파일 저장 완료')