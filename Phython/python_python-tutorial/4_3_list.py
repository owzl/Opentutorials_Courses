students = ["egoing", "sori", "maru"]
grades = [2, 1, 4]
print("students[1]", students[1])       # 리스트에서 인덱스 1에 해당하는 원소
print("len(students)", len(students))   # 해당 리스트의 원소 개수
print("min(grades)", min(grades))       # 해당 리스트에서 최소값인 원소
print("max(grades)", max(grades))       # 해당 리스트에서 최대값인 원소 
print("sum(grades)", sum(grades))       # 해당 리스트의 모든 원소의 합

# 통계와 관련한 여러 가지 기능이 있는 모듈 statistics
import statistics
print("statistics.mean(grades)", statistics.mean(grades))   # 해당 리스트의 모든 원소의 평균
# 평균 외에도 표준편차, 중앙값 등 쉽게 구할 수 있음


import random
print("random.choice(students)", random.choice(students))   # 해당 리스트 내 랜덤 원소
