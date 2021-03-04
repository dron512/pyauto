'''
    11.2.3 네임스페이스 패키지

단일 모듈 (.py 파일)
패키지 (모듈 및 다른 패키지를 포함하는 디렉터리)

네임스페이스 패키지가 있는 디렉터리에서 패키지를 분할 할 수도 있다.
실제 또는 상상 속에서 존재하는 위험한 생물에 대한 파이썬 모듈을 포함하는 critters 패키지가 있다고 가정하자
시간이 지나면서 패키지가 커질 수 있으므로 위치별로 세분화하려고 한다. 한가지 옵션은 critters 아래에 
하위 패키지를 추가하고 기존 .py 모듈 파일을 그 아래로 모두 이동한다. 그러나 이것은 이 모듈을 임포트한
다른 모듈에서 문제가 발생한다. 그대신 다음을 수행한다.

- critters 상위에 새 위치 디렉터리를 만든다.
- 새 상위 디렉터리 아래에 다른 종류으ㅟ 생물 디렉터리를 만든다.
- 기존 모듈을 해당 디렉터리로 이동한다

critters
aa.py
bb.py
from critters import aa,bb
'''
import sys
sys.path.insert(0,'E:\\py\\north')
sys.path.insert(0,'E:\\py\\south')

for path in sys.path:
    print(path)
from mymodule import aa,bb

aa.aa()
bb.bb()