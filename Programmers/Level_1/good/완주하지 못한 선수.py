def solution(participant, completion):
    # Case 1
    # participant.sort()
    # completion.sort()
    # for a, b in zip(participant, completion):
    #     if a!=b:
    #         return a
    # return participant[-1]

    ## Case 2
    import collections
    s = collections.Counter(participant) - collections.Counter(completion)
    return list(s.keys())[0]