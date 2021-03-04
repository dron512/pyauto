from datetime import *

some_day = datetime(2020,1,2,3,4,5,6)
print(some_day)
formatday = some_day.isoformat()
print(formatday)

now = datetime.now()

print(now)

noon = time(12)
noontoday = datetime.combine(now,noon)
print(noontoday)