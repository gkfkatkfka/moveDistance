'''
* 소스파일 이름 : 경기정보.py
* 소스파일 목적 : 경기 일정 정보 가져오기
* 세부 목적
: https://www.koreabaseball.com/Schedule/Schedule.aspx 데이터 크롤링
: 가져온 데이터를 구단별로 저장
* 완성 csv 속성 : 날짜, 경기, 구장
'''
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd


'''변수 리스트 설정'''
listYear=['2017', '2018', '2019', '2020', '2021'] # 연도 리스트
#listYear=['2017']

listMonth = ['04', '05', '06', '07', '08', '09', '10'] # 달 리스트
#listMonth = ['04']

listTeam = ['NC','OB','KT','LG','WO','HT','LT','SS','SK','HH'] # 팀 리스트(nc, 두산, kt, lg, 키움, 기아, 롯데, 삼성, ssg, 한화)
#listTeam = ['NC']

# 드라이버 가져오기
driver = webdriver.Chrome('C://Users//gkfka//Downloads//chromedriver_win32//chromedriver.exe')

# 사이트 열기
url=driver.get('https://www.koreabaseball.com/Schedule/Schedule.aspx')

# 정규 시즌 콤보 박스 클릭
driver.find_element_by_xpath("//select[@id='ddlSeries']/option[text()='KBO 정규시즌 일정']").click()


for team in listTeam:
    i=0

    # 결과 담을 리스트 초기화
    resultList=[]
    
    # 팀 선택
    driver.find_element_by_xpath("//ul[@class='tab-schedule']/li[@attr-value = '"+team+"']").click()

    # 연도 반복
    for year in listYear:
        # 연도 바꾸기
        driver.find_element_by_xpath("//select[@id='ddlYear']/option[text()='" + str(year) + "']").click()

        # 달 반복
        for month in listMonth:
            # 달 선택
            driver.find_element_by_xpath("//select[@id='ddlMonth']/option[text()='" + str(month) + "']").click()

            # 결과
            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')
            tblSchedule = soup.find('table', {'class': 'tbl'})
            trs = tblSchedule.find_all('tr')

            # 표 읽어오기
            for idx, tr in enumerate(trs):
                if idx > 0:
                    tds = tr.find_all('td')

                    # 1. null 값 거르기
                    if len(tds)==1:
                        continue

                    # 2. 특정 이벤트(취소, 더블헤더) 거르기
                    if len(tds[7].text.strip()) != 2:
                        continue

                    # 제2구장으로 쓰는 곳 제1구장으로 변환
                    if tds[7].text.strip() == '청주':  # 한화
                        tds[7] = '대전'
                    elif tds[7].text.strip() == '포항':  # 삼성
                        tds[7] = '대구'
                    elif tds[7].text.strip() == '울산':  # 롯데
                        tds[7] = '사직'
                    elif tds[7].text.strip() == '마산':  # nc
                        tds[7] = '창원'
                    else:
                        tds[7]=tds[7].text.strip()
                        
                    temp = [year, tds[0].text.strip(), tds[2].text.strip(), tds[7]]
                    
                    # 연속적인 장소 지우는 절차
                    if i!=0:
                        if temp[3] != resultList[-1][3]:
                            resultList.append(temp)
                    else:
                        resultList.append(temp)
                        i=i+1

    # csv 만들기
    data = pd.DataFrame(resultList)
    data.columns = ['year','date', 'score', 'place']
    data.head()
    data.to_csv('../데이터/팀별 경기정보/'+team + '.csv', encoding='UTF-8')
































