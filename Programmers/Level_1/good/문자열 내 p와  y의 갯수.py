def solution(s):
    # case 1
    s = s.lower()
    if s.count('p') == s.count('y'):
        return True
    else:
        return False
    
    ## case 2
    # if (s.count('p') + s.count('P'))== (s.count('y') + s.count('Y')):
