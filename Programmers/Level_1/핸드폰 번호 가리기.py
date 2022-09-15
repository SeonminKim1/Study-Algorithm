def solution(phone_number):
    ## case 1
    # return phone_number.replace(phone_number[:-4], "*"*len(phone_number[:-4]))
    
    ## case 2
    return '*'*(len(phone_number)-4) + phone_number[-4:]