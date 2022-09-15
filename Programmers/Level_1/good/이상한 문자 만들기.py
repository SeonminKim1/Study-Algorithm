def solution(s):
    # 짝수번째는 대문자로
    # 홀수번째는 소문자로
    ## case 1
    word_list = s.split(' ')
    answer_list = []
    for word in word_list:
        result = ''
        for i, w in enumerate(word):   
            if i%2: # 홀수면
                result += w.lower()
            else:
                result += w.upper()
        answer_list.append(result)
    return ' '.join(answer_list)

    ## case 2
    # return " ".join(map(lambda word: ''.join([w.lower() if i%2 else w.upper() for i, w in enumerate(word)]), s.split(' ')))