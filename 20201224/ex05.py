'''
11.3.1 누락된 키 처리하기 setdefault() 와 defaultdict()
딕셔너리에 존재하지 않는 키로 접근하면 예외가 발생한다. 기본값을 봔한하는 딕셔너리의 get함수를 사용하면
이 예외를 피할 수 있다. setdefault() 함수는 get() 함수와 같지만 키가 누락된 경우 딕셔너리에 항복을 할당할 수 있다

'''
# p_table = {'aa':'aaa','bb':'bbb'}
# print(p_table)
# p_table.setdefault('cc','ccc')
# print(p_table)

foodcount = {}
for food in ['egg','spam','spam','spam']:
    if not food in foodcount:
        foodcount[food] = 0
    foodcount[food] +=1
print(foodcount)

from collections import Counter
breakfast = ['egg','spam','spam','spam']
test = Counter(breakfast)
print(test)
print(test.most_common(1))