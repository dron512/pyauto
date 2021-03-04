'''
객체는 언제 사용할까
클래스 모듈의 사용지침은 다음과 같다
- 비슷한 행동(메서드)을 하지만 내부 상태(속성)가 다른 개별 인스턴스가 필요할 때, 객체는 매우 유용하다
- 클래스는 상속을 지원하지만, 모듈은 상속을 지원하지 않는다.
- 어떤 한가지 일만 수행한다면 모듈이 가장 좋은 선택일 것이다. 프로그램에서 파이썬 모듈이 참조된 횟수에 상관없이
단 하나의 복사본만 불러온다 ()
- 여러 함수에 인수로 전달하는 여러 변수가 있다면, 클래스를 정의하는 것이 더 좋다 예를 들어 화상 이미지를
나타내기 위해 size나 color를 딕셔너리의 키로 사용한다고 가정해보자. 프로그램에서 각 이미지에 대한 딕셔너리를 생성하고,
'''
from collections import namedtuple
from pprint import pprint

Duck = namedtuple('Duck','bill tail')
duck = Duck('wide orange','long')
print(duck)
print(duck.bill)
print(duck.tail)

parts = {'bill':'wide orange','tail':'long'}
duck2 = Duck(**parts)
print(duck2)

duck2 = Duck(bill='billllll',tail='longggg')
print(duck2)

duck3 = duck2._replace(tail='aaaa',bill='aabbb')
print(duck3)
print(duck3.bill)

my_dict = {'aa':'aaa','bb':'bbb'}
my_dict['cc']='ccc'
print(my_dict['cc'])

'''
네임드 튜플의 특징

-불변객체처럼 행동한다
-객체보다 공간 효율성과 시간 효율성이 더 좋다
딕셔너리 형식의 대괄호([] 대신, 온점(.)표기법으로 속성을 접근할 수 있다.
네임드 튜플을 딕셔너리 키처럼 사용할 수 있다.
'''
