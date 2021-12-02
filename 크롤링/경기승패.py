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

# 구장 식별 행, 열 반환
def switch(key):
    local = {"잠실": 1, "고척": 2, "문학": 3, "수원": 4, "대전": 5, "광주": 6, "대구": 7, "사직": 8, "창원": 9}.get(key, 0)
    return local

# 팀 이름 변환
def switchName(year,key):
	local=""
	if year<2018:
		local = { "OB": "두산", "WO": "넥센", "HT": "KIA", "SS": "삼성", "HH": "한화","LT":"롯데" }.get(key, key)
	elif year<2021:
		local = { "OB": "두산", "WO": "키움", "HT": "KIA", "SS": "삼성", "HH": "한화", "LT": "롯데" }.get(key, key)
	else:
		local = { "OB": "두산", "WO": "키움", "HT": "KIA", "SS": "삼성", "HH": "한화", "LT": "롯데","SK":"SSG"}.get(key, key)
	return local
 


# 구장 별 이동거리에 사용
moveArr = [] # 구장 별 이동거리 저장
distance = 0 # 거리
compareArr = []# 지역 담을 배열

# 필요한 리스트
listYear=['2017', '2018', '2019', '2020', '2021'] # 연도 리스트
listTeam = ['KT','WO','HT','LT','SS','HH','NC','SK','OB','LG'] # 팀 리스트(nc, 두산, kt, lg, 키움, 기아, 롯데, 삼성, ssg, 한화)

# 한글, 영어만 추출하는 정규식 => 팀명 추출할 때 사용
string = re.compile('[^ 가-힣 a-z A-Z]+')

# 거리 엑셀(크로스탭) 형식으로 되어 있는 것 불러오기
with open('../데이터/이동거리/거리 엑셀.csv', 'r', encoding='UTF-8') as distanceFile:
	distanceRead = csv.reader(distanceFile)
	
	# 들어온 데이터 정제
	for line in distanceFile:
		inArr = line.split(",")
		inArr[-1] = inArr[-1].replace("\n", "")
		moveArr.append(inArr)

for year in listYear:
	for team in listTeam:
		searchList = []
		teamArr = [0, ]
		compareArr = []
		
		# 파일 불러오기
		f = open('../데이터/년도별/'+year+'/'+year+team+'.csv', 'r', encoding='UTF-8')
		
		next(f)
		
		# csv 파일 헤더 제외 읽어오기
		information = csv.reader(f)
		
		# 정보 한 줄씩 불러와서 비교 배열 넣기
		for info in information:
			# 거리 가져오기
			compareArr.append(info[4])
			
			# 경기 내용(vs) 정보 가져오기
			strData = info[3]
			
			# vs로 일차적으로 문자열 분할
			strList = strData.split('vs')
	
			try:
				# 숫자만 추출
				firstScore = int(re.findall('\d+', strList[0])[0])
				secondScore = int(re.findall('\d+', strList[1])[0])
			except IndexError:
				# 경기취소나 이런걸로 경기 안 했을 경우
				firstScore = 0
				secondScore = 0
			
			# 팀만 추출
			firstTeam = string.sub('', strList[0])
			secondTeam = string.sub('', strList[1])
			
			# 0:패배 , 1: 승리
			if firstScore > secondScore and firstTeam == switchName(int(year),team):
				temp = [info[1], info[2], info[3], 1]
			elif firstScore < secondScore and secondTeam == switchName(int(year),team):
				temp = [info[1], info[2], info[3], 1]
			elif firstScore == secondScore:
				temp = [info[1], info[2], info[3], -1]
			else:
				temp = [info[1], info[2], info[3], 0, ]
			
			searchList.append(temp)

		# 현재와 이전 구장 사이의 거리 구하기(moveArr 이용)
		for i in range(1, len(compareArr) - 1):
			row = switch(compareArr[i - 1])
			col = switch(compareArr[i])
			
			distance = float(moveArr[row][col])
		
			teamArr.append(round(distance, 2))
		
			# csv 만들기
			data = pd.DataFrame(searchList)
			moveData = pd.DataFrame(teamArr)
			
			data = pd.concat([data, moveData], axis=1)
			data.columns = ['year', 'date', '경기', '승패여부', '거리']
			data.head()
			data.to_csv('../데이터/년도별_승률_거리/'+year+team+'.csv', encoding='UTF-8', index=False)






