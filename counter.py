from itertools import combinations, combinations_with_replacement

digits = [0,1,2,3,4,5,6,7,8,9]

def n_digits_combs(n):
    for comb in combinations(digits, n):
        print(("{}"*n).format(*comb))

def n_digits_combs_wr(n):
    for comb in combinations_with_replacement(digits, n):
        print(("{}"*n).format(*comb))