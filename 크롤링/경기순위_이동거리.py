'''
* 소스파일 이름 : 경기순위_이동거리.py
* 소스파일 목적 : 년도별 경기순위 데이터와 이동거리 데이터 합병
* 세부 목적
: 같은 값을 가진 데이터 합치기
: CSV로 저장
'''

import pandas as pd
# 필요한 리스트
listYear=['2017', '2018', '2019', '2020', '2021'] # 연도 리스트

moveFile=pd.read_csv("../데이터/이동거리/이동거리.csv")

for year in listYear:
	# 년도별 team 가져오기
	teamFile=pd.read_csv("../데이터/경기순위/"+year+".csv")

	# 팀별 년도별 csv 만들기
	data = pd.DataFrame(pd.merge(moveFile[['team',year]],teamFile,on='team'))
	data.to_csv('../데이터/경기순위_이동거리/'+year+'.csv', encoding='UTF-8',index=False)
