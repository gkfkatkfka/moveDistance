'''
* 소스파일 이름 : 경기순위_이동거리_병합.py
* 소스파일 목적 : 2017-2021년 순위 이동거리 병합(데이터프레임 하나로 만드려구)
* 세부 목적
: 2017-2021년 경기순위_이동거리 병합
'''
import pandas as pd
import matplotlib.pyplot as plt
import csv

listYear=['2017', '2018', '2019', '2020', '2021'] # 연도 리스트

# 데이터프레임 배열 만들기
dataArr=[]

for year in listYear:
	# team,
	f = open('../데이터/경기순위_이동거리/'+year+'.csv', encoding='UTF-8')
	
	next(f)
	
	# csv 파일 헤더 제외 읽어오기
	information = csv.reader(f)
	
	for info in information:
		dataArr.append(info)

print(dataArr)
# 팀별 년도별 csv 만들기
data = pd.DataFrame(dataArr)
data.columns = ['team', 'distance','rank','winRate']
data.head()
data.to_csv('../데이터/경기순위_이동거리/total.csv', encoding='UTF-8', index=False)

