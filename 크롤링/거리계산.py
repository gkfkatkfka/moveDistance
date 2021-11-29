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

# 필요한 리스트
listYear=['2017', '2018', '2019', '2020', '2021'] # 연도 리스트

listTeam = ['NC','OB','KT','LG','WO','HT','LT','SS','SK','HH'] # 팀 리스트(nc, 두산, kt, lg, 키움, 기아, 롯데, 삼성, ssg, 한화)
#listTeam = ['NC']

# 구단 별 이동거리 배열로 저장
moveArr = []  # 이동거리 저장 배열

with open('../데이터/거리 엑셀.csv', 'r', encoding='UTF-8') as distanceFile:
    distanceRead = csv.reader(distanceFile)
    
    # 들어온 데이터 정제
    for line in distanceFile:
        inArr = line.split(",")
        inArr[-1] = inArr[-1].replace("\n", "")
        moveArr.append(inArr)
