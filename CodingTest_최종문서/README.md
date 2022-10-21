### list
- list에서 특정 원소의 갯수 세기 : words.count(w)
- list에서 특정 원소('a')의 index 구하기 : words.index('a') - 첫번째 index 리턴함.
- list에서 특정 원소 들어있는지 찾기 : if 'a' in words
- list에서 모든 index 찾기 : [i for i, x in enumerate(l1) if x == 1]
- list에서 특정 원소값 제외하고 출력 : [x for x in q if x !=4]
- list에서 중복 제거시 set은 순서 정렬됨, OrderedDict는 순서 지켜짐
  - list(set(q))
  - list(OrderedDict.fromkeys(q)) - from collections import OrderedDict
- list에서 문자열 배열 정렬 : sorted(list1, key=lambda x:x[1]) // (list1 = ['bc','bd','ba'])
- list에서 tuple 배열 정렬 : list2.sort(key=lambda tup: tup[2]) // list2 = [('b',3,'cc'),('c',10,'aa'),('d',11,'dd')]
- list에서 2차원 슬라이싱 하기 sub_maps = [row[j:j+8] for row in maps[i:i+8]]
- list에서 역순 : list.reverse()  / list[::-1]
- list에서 swap : [a, b] = [b,a]

### Dict
- dictionary 에서 정렬
    - sorted(dict1.items()) // key 기반 정렬
    - sorted(dict1.items(), reverse=True) // 역순 정렬
    - sorted(dict1.items(), key = lambda x:x[1]) // value 기반 정렬

## Math
- 제곱근 구할때 => n**(1/2) 
- 소수점 확인 방법 n%1 != 0 인지 체크 (ex. 3.1 % 1 = 0.10009 / 3.0%1 = 0.0)
- from collections import Counter => Counter().most_common()
- 진법 변환
  - 10진수를 N진수로 : n, rest = divmod(n) // 몫과 나머지 반환하여 string 모음
  - N진수를 10진수로 : int('101', 2) // 2진수 101를 10진수 숫자로
  - 2진법, 8진법, 16진법 : bin, oct, hex

## 문자열
- lower(), upper() : 소문자로, 대문자로
- title : 문자의 각 단어 첫 글자 대문자, 나머지 소문자 // How Are You
- capitalize : 문장의 첫 글자만 대문자로, 나머지는 소문자 // How are you
- find() : 문자열 위치 찾음. 없으면 -1
- index() : 문자열 위치 찾음. 없으면 터짐
- startswith() : 지정된 문자로 시작하는지 체크 // True, False 반환
- endswith() : 지정된 문자로 끝나는지 체크 // True, False 반환
- isdigit() : 낱개의 문자가 숫자인지 // 0~9 , +, - 는 안됨
- isalpha() : 낱개의 문자가 알파벳인지
- isalnum() : 낱개의 문자가 알파벳 or 숫자 체크 // 공백안됨
- 문자열 분리하기 : split() - 모든 공백 기준 분리
- 문자열 뒤집기 : ('abc'[::-1]) or ''.join(reversed('abc'))
- 특정 문장에서 문자가 몇번 등장하는지 : count() // 'Hello world Hello hi fuck'.count('Hello')
- 정규식 (replace 함수는 정규식이 안됨)
  - 특정 문자 제외하고 치환하기 : re.sub('[^a-z0-9A-Z]', '', word)
  - 문자열에서 숫자 제외하기 : re.sub('[0-9]', '', word)
  - 모든 문자열의 문자와 숫자 빼고 공백으로 변경 : re.sub('[^\w]', ' ', paragraph) // \w는 알파벳 + 숫자 + _ 중의 한 문자 지칭
  - ^ : 특정 문자 시작, $:특정 문자 종료, +앞 패턴이 하나 이상, *앞 패턴이 0개 이상 (all)
  - [ ]  : 해당 문자들중 하나여야 함. (ex. [Pp]ython] => Python or python)
  - [^ ] : 해당 문자들을 제외한 나머지 (ex. [^aeiou] => 모음 제외한 나머지)
- 문자열 정렬하기 : sorted(data, key=lambda x:x[0]) // data = ['1 A', '1 B', '6 A', '2 D', '4 B'] 

## 기타
- from collections import deque => deque.popleft() appendleft() 가능

## 문자열 유형
- 회문(Palindrome) : 앞뒤가 똑같은 단어나 문장 (s = s[::-1]), 특수문자 제거시 re.sub()
- 가장 많이 등장하는 단어 찾기 : 정규식(특수문자 제거) + split로 list화 + Counter 실행 // paragraph = "Bob hit a ball, the hit BALL flew far after it was hit"

### 수학문제 구현 유형
- 약수의 합 i**(1/2) 써먹기 약수가 
- 소수 판별하기 => 2부터 root(N) 까지 나누기 ()
- 소수 구하기 => 에라토스테네스의 체

