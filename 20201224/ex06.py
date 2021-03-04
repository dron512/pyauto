'''
데크는 스택과 큐의 기능을 모두 가진 출입구가 양 끝에 있는 큐다. 데크는 시퀀스의 양 끝으로부터
항목을 추가하거나 삭제할 때 유용하게 쓰인다.
'''

def palindrome(word):
    from collections import deque
    dq = deque(word)
    # dq.append('cc')
    # dq.append('cc')
    # dq.append('cc')
    print(dq)
    while len(dq)>1:
        if dq.popleft() != dq.pop():
            return False
        return True

# print(palindrome('a'))
# print(palindrome('cac'))
# print(palindrome(''))
# print(palindrome('radar'))
# print(palindrome('halibut'))

import itertools
for item in itertools.chain([11,33],[22,44]):
    print(item)

from random import sample
print(sample([11,22,33],2))