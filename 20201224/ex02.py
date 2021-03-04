'''
데이터 클래스
많은 개발자는 행동(메서드)이 아니라 주로 데이터(속성)를 저장하기 위해 객체 생성하는 것을
선호한다. 이전 절에서 대체 할 수 있는 네임드 튜플을 살펴봤다. 파이썬 3.7부터는 데이터 클래스를 지원한다
name 속성을 가진 보통 객체는 다음과 같다
'''

class TeenyClass():
    def __init__(self,name):
        self.name = name

teeny = TeenyClass('enc')
print(teeny.name)

from dataclasses import dataclass
@dataclass
class TeenyDataClass:
    name : str

teeny = TeenyDataClass('aaa')
print(teeny.name)

'''
    Element 클래스에서 객체의 속성(name,symbol, number)값을 출력하는 dump()메서드를
    정의한다. 이 클래스의 hydrogen 객체를 생성하고 dump()메서드로 이 속성을 출력한다
'''

@dataclass
class Element:
    name : str
    symbol : str
    number : int
    def dump(self):
        print(vars(self))
    def __str__(self):
        return 'name : {} symbol : {} number : {}'.format(self.name,self.symbol,self.number)
hydrogen = Element(name='aa',symbol='!!!!@',number=1)
hydrogen.dump()
print(hydrogen)

'''
    print(hydrogen)을 호출한다 Element 클래스의 정의에서 dump 메서드를 __str__()
    메서드로 바꿔서 새로운 hydrogen 객체를 생성한다 그리고  print(hydrogen)을 다시 호출한다
'''

