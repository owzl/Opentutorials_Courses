# 각각의 원소에 이름을 붙일 수 있다면 얼마나 좋을까?
#['egoing', 'Seoul', 'Web']
#{'name':'egoing', 'address':'Seoul', 'interest':'Web'}

person = {'name':'egoing', 'address':'Seoul', 'interest':'Web'}
print(person['name'])
#           name이라는 키값의 value를 print

for key in person:
    print(key, person[key])
    # 리스트의 키값을 하나씩 꺼내서 key라는 이름의 변수의 값으로 할당

persons = [
    {'name':'egoing', 'address':'Seoul', 'interest':'Web'},
    {'name':'basta', 'address':'Seoul', 'interest':'IOT'},
    {'name':'blackdew', 'address':'Tongyeong', 'interest':'ML'}
]

print("==== persons ====")

for person in persons:
    #print(person)
    for key in person:
        print(key, ':', person[key])
    print('-------------------')
