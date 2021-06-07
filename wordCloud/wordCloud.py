import matplotlib.pyplot as plt
import nltk
import numpy as np
from wordcloud import WordCloud
from PyKomoran import Komoran
from wordcloud import ImageColorGenerator
from PIL import Image

##########################################################
#한글 깨짐을 막기위해 맑은 고딕으로 변경
plt.rc('font', family='Malgun Gothic')
filename = '31독립선언문 전문.txt'
#########################################################
#시각화를 위함 함수 생성 > 안만들어도되지만 객체지향적으로 처리하기위해서 클래스 생성함
class Visualization:
    #생성자
    def __init__(self, wordList):
        #리스트 생성
        self.wordList = wordList
        #list를 사전으로 변경
        self.wordDict = dict(wordList)
        #print(wordDict)
    #end def __init__(self, wordList)

    # 워드 클라우드(사진 색사용)
    def makeWordCloud02(self):
        pass
        color_file = '태극문양.png'
        # 넘파이로 불러온 그림 파일을 배열로 만들어줌
        coloring = np.array(Image.open(color_file))
        fontpath = 'malgun.ttf'
        # 워드클라우드 옵션주기
        wordcloud = WordCloud(font_path=fontpath, mask=coloring, \
                              relative_scaling=0.2, background_color='white')
        # 사전에 있는 빈도정보 가져와서 워드클라우드에 생성
        wordcloud = wordcloud.generate_from_frequencies(self.wordDict)
        # 사진 컬러로 글자 바꾸기
        image_colors = ImageColorGenerator(coloring)
        wordcloud = wordcloud.recolor(color_func=image_colors, random_state=42)
        plt.imshow(wordcloud)
        plt.axis('off')
        filename = 'wordCloud02.png'
        plt.savefig(filename, dpi=400, bbox_inches='tight')
        print(filename + ' 파일 저장 완료')
    # end def makeWordCloud(wordlist)

    # 워드 클라우드
    def makeWordCloud01(self):
        pass
        color_file = '태극문양.png'
        coloring = np.array(Image.open(color_file))
        fontpath = 'malgun.ttf'
        wordcloud = WordCloud(font_path=fontpath, mask=coloring, \
                              relative_scaling=0.2, background_color='white')
        wordcloud = wordcloud.generate_from_frequencies(self.wordDict)
        plt.imshow(wordcloud)
        plt.axis('off')
        filename = 'wordCloud01.png'
        plt.savefig(filename, dpi=400, bbox_inches='tight')
        print(filename + ' 파일 저장 완료')

#파일 읽어오기
ko_con_text = open(filename, encoding='utf-8').read()
#형태소 분석을위한 객체 생성
komo = Komoran('STABLE')
#명사만 추출
tokens_ko = komo.nouns(ko_con_text)
#불용어로 처리할 텍스트 생성
stop_word_file = 'stopword.txt'
#r:읽기,w:쓰기
stop_file = open(stop_word_file, 'rt', encoding='utf-8')
#리스트로 저장
stop_words = [word.strip() for word in stop_file.readlines()]
#불용어 제외
tokens_ko = [each_word for each_word in tokens_ko if each_word not in stop_words]
#단어를 하나하나씩 처리
ko = nltk.Text(tokens=tokens_ko)
#vocab 단어 / most_common 빈도
data = ko.vocab().most_common(250)
# wordlist =튜플(단어, 빈도수)을 저장할 리스트
wordlist = list()
for word, count in data :
    if (count >= 1 and len(word) >= 2):
        #()안의 (word, count) 튜플
        wordlist.append((word, count))

#생성자 생성
visual = Visualization(wordlist)
#객체
visual.makeWordCloud02()
visual.makeWordCloud01()
