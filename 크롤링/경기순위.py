'''
* 소스파일 이름 : 경기순위.py
* 소스파일 목적 : 경기 일정 정보 가져오기
* 세부 목적
: https://www.koreabaseball.com/TeamRank/TeamRank.aspx 데이터 크롤링
: 가져온 데이터를 년도별로 csv에 저장
* 완성 csv 속성 : 순위, 팀명, 승률
'''
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import time

'''변수 리스트 설정'''
listYear = ['2017', '2018', '2019', '2020', '2021']  # 연도 리스트
# listYear=['2017']

# 드라이버 가져오기
driver = webdriver.Chrome('C://Users//gkfka//Downloads//chromedriver_win32//chromedriver.exe')

i = 1

for year in listYear:
	resultArr = []
	
	url = driver.get('https://sports.news.naver.com/kbaseball/record/index?category=kbo&year=' + year)
	
	html = driver.page_source
	soup = BeautifulSoup(html, 'html.parser')
	tblSchedule = soup.find('div', {'class': 'tbl_box' })
	tbody = tblSchedule.find_all('tr')
	
	# 표 읽어오기
	for idx, tr in enumerate(tbody):
		if idx > 0:
			tds = tr.find_all('td')
			
			temp=[i,tds[0].text.strip(), tds[5].text.strip()]
			resultArr.append(temp)
			i = i+1
			
	# 팀별 년도별 csv 만들기
	data = pd.DataFrame(resultArr)
	data.columns = ['rank','team', 'winRate']
	data.head()
	data.to_csv('../데이터/경기순위/'+year + '.csv', encoding='UTF-8',index=False)




