# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/3/23 09:59

if __name__ == '__main__':
    # total money, total product
    n, m = map(int, input().split(' '))
    n //= 10
    # each product: price(v), weight(p), number(q)
    from collections import defaultdict
    prices = defaultdict(lambda: [0, 0, 0])
    values = defaultdict(lambda: [0, 0, 0])
    for i in range(1, m + 1):
        v, p, q = map(int, input().split(' '))
        v //= 10
        if q == 0:  # 主件
            prices[i][0] = v
            values[i][0] = v * p
        elif prices[q][1]:  # 追加附件
            prices[q][2] = v
            values[q][2] = v * p
        else:
            prices[q][1] = v
            values[q][1] = v * p

    # 0-1 package problem
    dp = [0] * (n + 1)
    # 买主件不一定买附件（最多买0-2个），但是买附件必须买主件
    for i, p in prices.items():
        p1, p2, p3 = p
        v1, v2, v3 = values[i]
        for j in range(n, p1 - 1, -1):
            # 四种情况00,01,10,11
            if j >= p1:
                dp[j] = max(dp[j], dp[j - p1] + v1)
            if j >= p1 + p2:
                dp[j] = max(dp[j], dp[j - p1 - p2] + v1 + v2)
            if j >= p1 + p3:
                dp[j] = max(dp[j], dp[j - p1 - p3] + v1 + v3)
            if j >= p1 + p2 + p3:
                dp[j] = max(dp[j], dp[j - p1 - p2 - p3] + v1 + v2 + v3)
    print(dp[n] * 10)



