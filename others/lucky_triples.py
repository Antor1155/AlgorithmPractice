def solution(l):
    # Your code here
    if len(l) < 3:
        return 0
    lucky_triples = 0
    
    ele_double =[0] * len(l)
    
    for ind in range(1, len(l)):
        for pre_ind in range(ind):
            if l[ind] % l[pre_ind] == 0:
                ele_double[ind] += 1
                lucky_triples += ele_double[pre_ind]
    return lucky_triples

    print(double_of_pre)
    print(lucky_triples)

print(solution([1, 1, 2, 11, 4]))