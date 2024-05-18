#price = 1000
#vat_rate = 0.1
#print(price*vat_rate)
# 1억

            # 매개변수 Parameter: 그 인자를 받아서 함수 안에서 사용하는 변수
def get_vat(price, vat_rate=0.1):
    # price = 1000
    # vat_rate = 0.1
    return print(price*vat_rate)

# return을 만나면 함수의 실행이 끝나고
# 그리고 return 뒤에 있는 값이 그 함수의 값이 되는 것이다

# 이 함수의 기능
# 1. 부가가치세 계산
# 2. 그 값을 출력

# 값을 리턴하려면 return

        # 전달안했을 때 default 값 설정하려면 위의 =0.1처럼 기입
get_vat(10000) # 인자 Argument: 함수의 입력값으로 전달한 값
get_vat(20000, 0.3)

print(get_vat(10000))
# email.send('egoing@gamil.com', get_vat(20000, 0.3)

# 서로 관련된 코드를 모아서 이름을 붙여 => 함수
# 입력값을 만들고 그 입력값에 따라 다르게 동작하는 것 만들고 싶다면? => 변수 전달