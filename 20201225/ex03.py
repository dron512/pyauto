from datetime import *

dayofweek = ['월','화','수','목','금','토','일']
now = datetime(1985,5,11)
print(dayofweek[now.weekday()])
day10000 = timedelta(days=13000)
print(now+day10000)


'''
print(datetime.today().isoformat())
noon = time(12)
print(noon)

import time
print(time.ctime(time.time()))

fmt = '%A %B %d'
some_day = datetime.today()
fsome_day = some_day.strftime(fmt)

print(fsome_day)



문자열을 날짜나 시간으로 변환하기 위해 같은 포맷 문자열로 strptime()을 사용한다. 정규 표현식 패턴 매칭은 없다
문자열의 비형식 부분(% 제외)이 정확히 일치해야 한다. 2019-01-29와 같이 년-월-일이 일치하는 포맷을 지정해보자.
날짜 문자열에서 대시(-)대신 공백을 사용하면 무슨일이 일어날까?
'''



