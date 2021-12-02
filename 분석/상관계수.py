'''
* 소스파일 이름 : 상관계수.py
* 소스파일 목적 : 2017-2021년 상관계수 파악
* 세부 목적
: 2017-2021년 순위 상관계수 구하기
: 2017-2021년 승률 상관계수 구하기
'''
import pandas as pd

df =  pd.read_csv('../데이터/경기순위_이동거리/total.csv', encoding='UTF-8')

corrData = df[['distance','rank','winRate']]

# 두 변수간의 상관관계 분석
corr1 = corrData['distance'].corr(corrData['rank'])
corr2 = corrData['distance'].corr(corrData['winRate'])

print('rank 상관계수: ', corr1)#-0.119073308443464
print('winRate 상관계수: ', corr2)
