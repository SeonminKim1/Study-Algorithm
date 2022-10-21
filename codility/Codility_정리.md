### Codility 문제 유형
- **1. 반복 (Iterations)**
- **2. 배열 (Arrays)**
- **3. 시간 복잡도 트레이닝(Time Complexity)**
- **4. 요소 세기(Couting Element)**
- **5. 프리픽스 합계(Prefix sum)**
- 6. 정렬(Sorting)
- 7. 스택과 큐(Stack and Queues)
- **8. 선두자(Leader)**
- **9. 최대 조각 문제(Maximum slice problem) : dynamic - 카데인 알고리즘**
- **10. 프라임과 컴포지트 숫자(Prime and composite numbers) - 소수와 합성수**
- **11. 에라스토텔레스의 체(Sieve of Eratoshtheness) - 임의의 값보다 작은 소수 구하기**
- **12. 유클리디안 알고리즘(Euclidean algorithm) - 유클리드 호제법 외우기**
- **13. 피보나치 수열(Fibonacci numbers)**
- 14. 이진 검색 알고리즘(Binary Search algorithm) - 이분탐색
- 15. 캐터필러 방법(Caterpillar method) - 투포인터
- 16. 탐욕 알고리즘(Greedy algorithm)
- 17. 동적 프로그래밍(Dynamic programing)

### 주의사항
- 항상 꼼꼼하게 코딩
- input.txt 에서 테스트 엄청넣어보기
- 먼저 performance 고려 없이 먼저 풀기

### 자주 나오는 wording
- consecutive : 연속적인
- nested : 중첩
- consider : 고려하다
- distinct : 구별된 (m과 w는 구별된)
- more than, greater than : 초과 (번역은 이상으로 되지만.. 수학에선 초과임!)
- not less than, greater than or equal to : 이상
- not more than, smaller than or equal to : 이하
- equals : =
- not equal to : !=
- A non-empty array A : 가 주어짐

### 수학관련 영단어
- divisr or factors (약수) / multiple (배수) / a common divisor (공약수) / a common multiple (공배수)
- the greatest common divisor (최대공약수, GCD) / the least common multiple (최소공배수, LCM)
- prime number (소수), composition (합성수)
- odd (홀수), even (짝수)

### 다시 풀어볼 문제
- lesson_3_TapeEquilibrium.py (o)
- lesson_4_PermCheck.py (o)
- lesson_4_MaxCounters.py (o)
- lesson_5_PassingCars.py (o)
- lesson_6_Triangle.py (o)
- lesson_6_NumberOfDiscIntersections.py (o)
- lesson_7_Brackets.py (o)
- lesson_8_Dominator.py
- lesson_8_EquiLeader.py
- lesson_9_MaxProfit.py
- lesson_9_MaxSliceSum.py

### 카데인 알고리즘(Kadane's algorithm)
- 배열의 최대 부분 합을 O(n)의 시간복잡도로 구하는 알고리즘
- 최대 부분 합이 음수이면 굳이 더하지 않고 그냥 i+1번째 인덱스부터 새로 더하는게 당연히 이득이기 때문

### 문자열 유형
- 회문(Palindrome) : 앞뒤가 똑같은 단어나 문장 (s = s[::-1]), 특수문자 제거시 re.sub()
- 가장 많이 등장하는 단어 찾기 : 정규식(특수문자 제거) + split로 list화 + Counter 실행 // paragraph = "Bob hit a ball, the hit BALL flew far after it was hit"

### 수학문제 구현 유형
- 약수의 합 i**(1/2) 써먹기 약수가 
- 소수 판별하기 => 2부터 root(N) 까지 나누기 ()
- 소수 구하기 => 에라토스테네스의 체

### 예상 문제
- 1.문자열 : 주어진 문자열 검색, 제거 분리 특정한 문자열을 만드는 문제
- 2.문자열 : 주어진 문자열 비교, 검색, 분리하여 조건에 맞는 특정 문자열들의 갯수를 찾는 문제
- 3.해쉬 : 주어진 배열에서 HashMap을 이용해 중복을 제거하는 문제

### 수학 & 문자열 관련 코딩테스트 준비
- https://gyyeom.tistory.com/51
- https://velog.io/@norighthere/%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8%EC%97%90-%EC%82%AC%EC%9A%A9-%EB%90%98%EB%8A%94-%EC%88%98%ED%95%99 
- https://han-py.tistory.com/331
- https://han-py.tistory.com/334

