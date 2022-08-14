# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/3/10 7:12 PM

if __name__ == "__main__":
        # n, m = 5, 4
        # a = [0] + [0, 0, 4, 1, 1]
        # init_pos = [5, 4, 2, 2]
        n, m = map(int, input().split())
        a = [0] + list(map(int, input().split()))
        init_pos = list(map(int, input().split()))
        for i in init_pos:
            a[i] -= 1
        # 最后剩余房间数, 让多余的房间不要往上走
        left_home = sum(a)
        # 松鼠走过的距离
        res = 0
        # 层次遍历，从最后一层开始，每层的松鼠只能往上走
        # 如果有多余的房间，我们让房间也往上走
        # 每次往上走的时候，增加走过的距离
        for i in range(n, 0, -1):
            if a[i] != 0:
                if left_home > 0 and a[i] > 0:
                    if left_home > a[i]:
                        left_home -= a[i]
                    else:
                        a[i // 2] += a[i] - left_home
                        res += a[i] - left_home
                        a[i] = 0
                    continue
                a[i // 2] += a[i]
                res += abs(a[i])
                a[i] = 0
        print(res)