def f(L1, L2):
    """L1,L2は同じ長さの数値リストである
    L１の各要素に対してL2の同じ添字の要素で冪乗し、その和を返す
    例えば、f([1,2],[2,3]は9を返す)"""
    return sum(map(lambda i: L1[i]**L2[i], range(len(L1))))
print(f([1,2],[2,3]))