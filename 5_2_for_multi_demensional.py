persons = [
    ['egoing', 'Seoul', 'Web'],
    ['basta', 'Seoul', 'IOT'],
    ['blackdew', 'Tongyeong', 'ML'],
]

# egoing
print(persons[0][0])


#egoing,Seoul,Web
#basta,Seoul,IOT
#blackdew,Tongyeong,ML

for person in persons:
    print(person[0] + ',' + person[1] + ',' + person[2])


# 이름을 붙여서 더 분명하게 표현하기
# 위쪽에서 리스트 하나만 가져와서
person = ['egoing', 'Seoul', 'Web']
name = person[0]
address = person[1]
interest = person[2]
print(name, address, interest)
# 위의 과정을 더 간편하게?
name, address, interest = ['egoing', 'Seoul', 'Web']
print(name, address, interest)

# 이를 활용해 위의 반복문을 개선하자면?
# 인덱스에 따라 데이터를 가져오니까 코드를 해석하는게 어려웠음
for name, address, interest in persons:
    print(name + ',' + address + ',' + interest)

# 이전과 똑같은 결과가 나오지만 훨씬 코드를 해석하기 좋다