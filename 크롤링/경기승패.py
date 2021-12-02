'''
* 소스파일 이름 : 경기승패.py
* 소스파일 목적 : 원정거리와 승패여부
* 세부 목적
: '데이터/년도별/0000xx.csv'에 거리 추가
: '데이터/년도별/0000xx.csv'에 승패여부 추가
: 저장
'''
import re
import csv
import pandas as pd

def switchName(key):
    local = { "OB": "두산", "키움": "WO", "넥센": "WO", "KIA": "HT", "삼성": "SS", "SSG": "SK", "한화": "HH"}.get(key, key)
    #local = { "NC": "NC", "OB": "두산", "KT": "KT", "LG": "LG", "대전": 5, "광주": 6, "대구": 7, "사직": 8, "창원": 9}.get(key, key )
    return local

def switch(key):
    local = {"잠실": 1, "고척": 2, "문학": 3, "수원": 4, "대전": 5, "광주": 6, "대구": 7, "사직": 8, "창원": 9}.get(key, 0)
    return local


# 구장 별 이동거리 배열로 저장
moveArr = []  # 이동거리 저장 배열

# 나중에 여기서 에러나면 거리 엑셀.csv가 경로에 잘 있는지 확인
with open('../데이터/이동거리/거리 엑셀.csv', 'r', encoding='UTF-8') as distanceFile:
	distanceRead = csv.reader(distanceFile)
	
	# 들어온 데이터 정제
	for line in distanceFile:
		inArr = line.split(",")
		inArr[-1] = inArr[-1].replace("\n", "")
		moveArr.append(inArr)
		
# 한글, 영어만 추출하는 정규식 => 팀명 추출할 때 사용
string = re.compile('[^ 가-힣 a-z A-Z]+')
searchList = []

# 지역 담을 배열
compareArr = []

# 파일 선택
f = open('../데이터/년도별/2017/2017HH.csv', 'r', encoding='UTF-8')

next(f)

# csv 파일 하나를 읽어옴
information = csv.reader(f)

# 헤더 데이터 안 읽어오기
header = next(information)

distance = 0

# 정보 한 줄씩 불러오기
for info in information:
	strData = info[3]
	compareArr.append(info[4])
	
	# vs로 일차적으로 문자열 분할
	strList = strData.split('vs')
	
	print(strList)
	
	# 현재와 이전 구장 사이의 거리 구하기(moveArr 이용)
	for i in range(1, len(compareArr) - 1):
		row = switch(compareArr[i - 1])
		col = switch(compareArr[i])
		
		distance = float(moveArr[row][col])
	
	try:
		# 숫자만 추출
		firstScore = int(re.findall('\d+', strList[0])[0])
		secondScore = int(re.findall('\d+', strList[1])[0])
	except IndexError:
		firstScore=0
		secondScore=0

	
	# 팀만 추출
	firstTeam = string.sub('', strList[0])
	secondTeam = string.sub('', strList[1])
	
	# 0:패배 , 1: 승리
	if firstScore > secondScore and firstTeam == "한화":
		temp = [info[1],info[2], info[3], 1,distance]
	elif firstScore < secondScore and secondTeam == "한화":
		temp = [info[1],info[2], info[3], 1,distance]
	elif firstScore==secondScore:
		temp = [info[1], info[2], info[3], -1,distance]
	else:
		temp = [info[1],info[2], info[3], 0,distance]
	
	searchList.append(temp)
	
	# csv 만들기
	data = pd.DataFrame(searchList)
	data.columns = ['year','date', '경기', '승패여부','거리']
	data.head()
	data.to_csv('../데이터/년도별/2017/2017HHtest.csv', encoding='UTF-8',index=False)
	
	