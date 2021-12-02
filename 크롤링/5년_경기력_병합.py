'''
* 소스파일 이름 : 5년_경기력_병합.py
* 소스파일 목적 : 2017-2021년 경기력 병합
* 세부 목적
: 2017-2021년 year,date,경기,승패여부,거리
: csv 만들기
'''
import csv
import pandas as pd

# 필요한 리스트
listYear=['2017', '2018', '2019', '2020', '2021'] # 연도 리스트
listTeam = ['KT','WO','HT','LT','SS','HH','NC','SK','OB','LG'] # 팀 리스트(nc, 두산, kt, lg, 키움, 기아, 롯데, 삼성, ssg, 한화)

# 데이터프레임 배열 만들기
dataArr=[]

for year in listYear:
	for team in listTeam:
		f = open('../데이터/년도별_승률_거리/'+year+'/'+ year +team+'.csv', encoding='UTF-8')
		
		next(f)
		
		# csv 파일 헤더 제외 읽어오기
		information = csv.reader(f)
		
		for info in information:
			temp=[info[3],info[4]]
			dataArr.append(temp)
	
print(dataArr)

# 팀별 년도별 csv 만들기
data = pd.DataFrame(dataArr)
data.columns = ['승패여부','거리']
data.head()
data.to_csv('../데이터/년도별_승률_거리/total.csv', encoding='UTF-8', index=False)

