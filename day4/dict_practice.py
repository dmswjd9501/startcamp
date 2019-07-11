"""
Python dictionary 연습 문제
"""

# 1. 평균을 구하시오.
score = {
    '수학': 80,
    '국어': 90,
    '음악': 100
}

# 아래에 코드를 작성해 주세요.

# 1. 기본 풀이
print('==== Q1 ====')
result = 0  # 비어있는 통을 만들어놓고 더해줘야해. for문 안으로 넣어버리면 마지막값만 더해지게 된다.
for score_value in score.values():
    result = result + score_value 
print(result/len(score))

# 1-1. 좀 무식하게 보여도, 기억이 안나면 이렇게라도 len 카운트 해줘야함
result = 0
count = 0
for score_value in score.values():
    result = result + score_value
    count = count + 1   # 자기자신에게 더해주려면 result += score_value 이렇게 써줌
print(result/count)


# 2. sum 함수 활용하기
result2 = sum(score.values()) # sum 함수는 숫자가 나열된 형태를 다 더해준다.
count = len(score)
print(result2/count)

# 2. 학생들의 전체 평균을 구하시오.
scores = {
    'a': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    },
    'b': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    }
}

# 1. 기본 풀이
print('==== Q2 ====')
total_score = 0
count = 0
for person_scores in scores.values():
    for score in person_scores.values():
        total_score += score
        count += 1
print(total_score/count)

# 3. 도시별 최근 3일의 온도입니다.
city = {
    '서울': [-6, -10, 5],
    '대전': [-3, -5, 2],
    '광주': [0, -2, 10],
    '부산': [2, -2, 9],
}

# 3-1. 도시별 최근 3일의 온도 평균은?

# 아래에 코드를 작성해 주세요.
print('==== Q3-1 ====')
"""
출력 예시) # 키랑 값이 모두 필요하기 때문에 items로 뽑아야한다/
서울 : 값
대전 : 값
광주 : 값
부산 : 값
"""
for name, temp in city.items():
    avg = sum(temp) / len(temp)
    print(f'{name} : {avg:.2f}') # f-string : 3.6+ # 소수점 둘째자리까지 하고 싶으면 .2f
    print('{} : {:.2f}'.format(name, avg)) # format-string
    print(name + ':' + avg)



# 3-2. 도시 중에 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?

# 아래에 코드를 작성해 주세요.
print('==== Q3-2 ====')

min_temp = 0
max_temp = 0
min_city = ''
max_city = ''
# 모든 지역의 온도를 모두 확인하면서,
for name, temp in city.items():
    # 첫번째 반복때는 모두 다 저장해!
    if count == 0:
        min_city = name
        max_city = name
        min_temp = min(temp)
        max_temp = max(temp)
        count += 1
# 가장 추우면, 해당 도시와 기온을 기록
    if min(temp) < min_temp:
        min_city = name
        min_temp = min(temp)
# 더울 때도, 해당 도시와 기온을 기록
    if max(temp) > max_temp:
        max_city = name
        max_temp = max(temp)
print(f'추운 곳은 {min_city}, 더운곳은 {max_city}')

# 3-3. 위에서 서울은 영상 2도였던 적이 있나요?

# 아래에 코드를 작성해 주세요.
print('==== Q3-3 ====')

if 2 in city['서울']:
    print('네')
else:
    print('아니오') 
    
# 어떤 리스트안에 어떤 값이 있냐? 라는 함수가 있다. if문안에서의 in => 존재여부 물어보는것
# python에서 'a' in 'apple' => True
# 1 in [1, 2, 3] => True
# 0 in range(5) => True