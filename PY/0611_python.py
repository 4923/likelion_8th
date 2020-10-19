# 리스트
li = [3, 1, '배가', 4, '고파요', 5, 1]

# 인덱싱
print(li[2])

# 슬라이싱
print(li[0:3])

# 리스트 (내장함수)
li = [3, 1, '배가', 4, '고파요', 5, 1]
li_2 = [3, 1, 2, 4, 9, 5, 1]

# 리스트의 길이를 구해주는 함수 - len(변수)
print(len(li))

# 리스트의 원소 오름차순 정렬하는 함수 - 변수.sort()
li_2.sort()
print(li_2)

# 리스트 내의 특정 원소 인덱스를 반환해주는 함수 - .count(특정원소)
print(li.count(1))

#===

# 딕셔너리 (내장함수)
pairs = {'지코':'아무노래', '오반':'어떻게 지내', '크러쉬':'가끔'}
print(pairs)

# 하나의 key-value 쌍을 추가하는 방법
# 딕셔너리명 변수[키] = value
pairs['Maroon 5'] = 'Memories'
# 4번째 key-value 쌍을 추가했어요!
print(pairs)

# 특정 key-value 삭제하는 방법 : del 함수
del pairs['지코']
print(pairs)

# key로 value 열기 : 변수.get(키)
v = pairs.get('오반')
print(v)

# ===

#튜플 생성
tp = (1, 2, 3)
tp2 = (4, 5, 6)

#튜플의 덧셈
print(tp + tp2)
#튜플의 곱셈
print(tp * 3)
#튜플의 인덱싱
print(tp[0])
#튜플의 슬라이싱
print(tp[0:3])