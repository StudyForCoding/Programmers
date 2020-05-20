from itertools import product
from collections import defaultdict

def solution(clothes):
    answer = 0
    dic= defaultdict(list)
    for one_cloth in clothes:
        dic[one_cloth[1]].append(one_cloth[0])

    kind_list = list(dic.keys())
    name_list = list(dic.values())

    len_kind_list = len(kind_list)
    len_name_list = len(name_list)
    all_count = 1 << len_name_list
    
    if len_kind_list == 1:
        return len(clothes)
    if len_kind_list == len(clothes):
        return all_count - 1
    
    for n in range(1, all_count): #제거할 카운트 만큼
        num = n
        idx = len_kind_list - 1
        temp = []
        while num != 0:
            if num % 2 != 0:
                temp.append(name_list[idx])
            num = num//2
            idx -= 1
        answer += len(list(product(*temp)))
    return answer