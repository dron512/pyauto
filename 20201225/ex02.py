'''
파이썬에서 datetime 모듈의 time 객체와 별도의 time 모듈이 헷갈린다. 더군다나 time 모듈에는 time()이라는 함수가 있다
절대 시간을 나타내는 한가지 방법은 어떤 시작점 이후 초를 세는 것이다. 유닉스 시간은 1970년 1월 1일 자정 이후 시간의
초를 사용했다. 이 값을 에폭이라고 부르며 에폭은 시스템 간에 날짜와 시간을 교환하는 아주 간단한 방식이다.
'''

import time

now = time.time()
print(now)

today_now = time.ctime(now)
print(today_now)

'''
에폭 값은 자바스크립트 와 같은 다른 시스템에서 날짜와 시간을 교환하기 위한 유용한 최소 공통분모이다.
그리고 각각의 날짜와 시간 요소를 얻기 위해  time 모듈의 struct_time 객체를 사용할 수 있다.
localtime()메서드는 시간을 시스템의 표준 시간대로, gmtime()메서드는 시간을 UTC로 제공한다.
'''

print(time.localtime(now))
print(time.gmtime(now))



'''
19:55(중부 표준시, 일광 절약 시간제)은 UTC(이전에는 그리니치 시간 또는 줄루 시간)로 다음날 00:55이다.
localtime() 혹은 gmtime()에서 인수를 생략하면 현재 시간으로 가정한다.

mktime() 메서드는 struct_time객체를 에폭초로 변환한다.

몇가지 조언 표준 시간대 대신 UTC를 사용하는걸 추천한다. UTC는 표준 시간대와 독립적인 절대 시간이다
서버 운영하고 있다면 현지 시간이 아닌 UTC로 설정하자
더 만은 조언 일광 절약 시간은 사용하지 않는 것이 좋다 이것을 사용하면 연중 한 시간이 한번에 사라지고 
'''

'''
isoformat()이 날짜와 시간을 쓰기 위한 유일한 방법은 아니다 time모듈에서 본 ctime()
함수로 쓸 수 있다. 이함수는 에폭시간을 문자열로 변환한다.
'''



