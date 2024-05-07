import pandas
house = pandas.read_csv('house.csv')
# house.csv 파일안에 있는 데이터를 보기 좋게 시각화하여 보여줌
print(house)
# 초반에 있는 데이터만 출력하기(5개가 기본)
print(house.head())
# 초반에 있는 2개의 데이터만 출력하기
print(house.head(2))

# 표에 대한 정보 묘사, 각각의 컬럼의 성격을 파악하고 싶다
print(house.describe())