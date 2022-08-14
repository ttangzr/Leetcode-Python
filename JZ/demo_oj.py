# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/2/18 6:27 PM

# number
def test0():
    import sys
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    ans = 0
    for i in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        values = list(map(int, line.split()))
        for v in values:
            ans += v
    print(ans)

def test1():
    """
    input:
        1 5
        10 20
    output:
        6
        30
    """
    while True:
        try:
            l = list(map(int, input().split()))
            print(sum(l))
        except:
            break

def test2():    # mark
    """
    input:
        2
        1 5
        10 20
    output:
        6
        30
    """
    while True:
        try:
            n = int(input())
            for i in range(n):
                print(sum(list(map(int, input().split()))))
        except:
            break

def test3():
    """
    input:
        1 5
        10 20
        0 0
    output:
        6
        30
    """
    while True:
        l = list(map(int, input().split()))
        if l[0] != 0 and l[1] != 0:
            print(sum(l))
        else:
            break

def test4():
    """
    input:
        4 1 2 3 4
        5 1 2 3 4 5
        0
    output:
        10
        15
    """
    while True:
        l = list(map(int, input().split()))
        if l[0] != 0:
            print(sum(l[1:]))
        else:
            break

def test5():
    """
    input:
        2
        4 1 2 3 4
        5 1 2 3 4 5
    output:
        10
        15
    """
    while True:
        n = int(input())
        if n:
            for i in range(n):
                l = list(map(int, input().split()))
                print(sum(l[1:]))
        else:
            break

# string
def test6():
    """
    input:
        5
        c d a bb e
    output:
        a bb c d e
    """
    while True:
        n = int(input())
        s = sorted(input().split())
        print(' '.join(s))

def test7():
    """
    input:
        a,c,bb
        f,dddd
        nowcoder
    output:
        a,bb,c
        dddd,f
        nowcoder
    """
    while True:
        s = sorted(input().split(','))
        print(','.join(s))


if __name__ == "__main__":
    test7()