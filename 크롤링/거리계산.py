'''
* 소스파일 이름 : 거리계산.py
* 소스파일 목적 : 년도별 팀별 이동거리 구하기
* 세부 목적
: '../데이터/팀별 경기정보' 안에 있는 데이터는 가져오기
: 년도별 팀별 가져오기(year로 년도별 정보 가져오기)
: 년도별 csv 파일로 저장(구단, 이동거리)
: '../데이터/이동거리'에 년도별 저장
'''
import pandas as pd
import csv

def switch(key):
    local = {"잠실": 1, "고척": 2, "문학": 3, "수원": 4, "대전": 5, "광주": 6, "대구": 7, "사직": 8, "창원": 9}.get(key, 0)
    return local

# 필요한 리스트
listYear=['2017', '2018', '2019', '2020', '2021'] # 연도 리스트

listTeam = ['NC','OB','KT','LG','WO','HT','LT','SS','SK','HH'] # 팀 리스트(nc, 두산, kt, lg, 키움, 기아, 롯데, 삼성, ssg, 한화)
#listTeam = ['NC']

# 구단 별 이동거리 배열로 저장
moveArr = []  # 이동거리 저장 배열

# 거리 합
distance = 0

with open('../데이터/거리 엑셀.csv', 'r', encoding='UTF-8') as distanceFile:
    distanceRead = csv.reader(distanceFile)
    
    # 들어온 데이터 정제
    for line in distanceFile:
        inArr = line.split(",")
        inArr[-1] = inArr[-1].replace("\n", "")
        moveArr.append(inArr)

#print(moveArr)

# 2017HH만 해보기
f = open('../데이터/년도별/2017/2017HH.csv', 'r', encoding='UTF-8')

# csv 파일 하나를 읽어옴
information = csv.reader(f)

# 헤더 데이터 안 읽어오기
header = next(information)

compareArr=[]

# 정보 한 줄씩 불러오기
for info in information:
    compareArr.append(info[4])

print(compareArr)

for i in range(1,len(compareArr)-1):
    #$print(compareArr[i])
    row = switch(compareArr[i-1])
    col= switch(compareArr[i])

    distance += float(moveArr[row][col])
    print(moveArr[row][col])

print(distance)

