'''
* 소스파일 이름 : 거리계산.py
* 소스파일 목적 : 년도별 팀별 이동거리 구하기
* 세부 목적
: '../데이터/팀별 경기정보' 안에 있는 데이터는 가져오기
: 년도별 팀별 가져오기(year로 년도별 정보 가져오기)
: 년도별 csv 파일로 저장(구단, 이동거리)
: '../데이터/이동거리'에 년도별 저장
'''
import csv
import pandas as pd

# 구장 식별 행, 열 반환
def switch(key):
    local = {"잠실": 1, "고척": 2, "문학": 3, "수원": 4, "대전": 5, "광주": 6, "대구": 7, "사직": 8, "창원": 9}.get(key, 0)
    return local

# 필요한 리스트
listYear=['2017', '2018', '2019', '2020', '2021'] # 연도 리스트
listTeam = ['NC','OB','KT','LG','WO','HT','LT','SS','SK','HH'] # 팀 리스트(nc, 두산, kt, lg, 키움, 기아, 롯데, 삼성, ssg, 한화)

# 자료 담을 배열
csvArr=[['year','NC','OB','KT','LG','WO','HT','LT','SS','SK','HH']]

# 구장 별 이동거리 배열로 저장
moveArr = []  # 이동거리 저장 배열

with open('../데이터/거리 엑셀.csv', 'r', encoding='UTF-8') as distanceFile:
    distanceRead = csv.reader(distanceFile)
    
    # 들어온 데이터 정제
    for line in distanceFile:
        inArr = line.split(",")
        inArr[-1] = inArr[-1].replace("\n", "")
        moveArr.append(inArr)


for year in listYear:
    # 같은 년도 팀들의 배열
    teamCsvArr=[year,]

    for team in listTeam:
        # 거리 합
        distance = 0

        # 지역 담을 배열
        compareArr = []

        # 파일 불러오기
        f = open('../데이터/년도별/'+year+'/'+year+team+'.csv', 'r', encoding='UTF-8')

        next(f)

        # csv 파일 헤더 제외 읽어오기
        information = csv.reader(f)

        # 정보 한 줄씩 불러와서 비교 배열 넣기
        for info in information:
            compareArr.append(info[4])

        # 현재와 이전 구장 사이의 거리 구하기(moveArr 이용)
        for i in range(1, len(compareArr) - 1):
            row = switch(compareArr[i - 1])
            col = switch(compareArr[i])

            distance += float(moveArr[row][col])

        #print(year,team)
        #print(round(distance,2))
        teamCsvArr.append(round(distance, 2))

    csvArr.append(teamCsvArr)

# csv 저장
dataframe=pd.DataFrame(csvArr)
dataframe.to_csv("../데이터/이동거리/이동거리.csv", header=False, index=False)

