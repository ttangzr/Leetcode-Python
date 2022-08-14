# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/2/17 8:44 AM


class Solution:
    def countPrimes(self, n: int) -> int:
        # method-1: enumerate (timeout)
        # ans = 0
        # for i in range(2, n):
        #     ans += self.isPrime(i)
        # return ans

        # method-2: 埃氏筛
        is_prime = [1] * n
        ans = 0
        for i in range(2, n):
            if is_prime[i] == 1:
                ans += 1
                # start from x**2, 2*x, 3*x, ...->0
                for j in range(i * i, n, i):
                    is_prime[j] = 0
        return ans

        # method-3: 线性筛
        is_prime = [1] * n
        primes = list()
        for i in range(2, n):
            if is_prime[i] == 1:
                primes.append(i)
            for j in range(len(primes)): # x*prime_0, x*prime_1, ..., n
                if i * primes[j] >= n:
                    break
                is_prime[i * primes[j]] = 0
                if i % primes[j] == 0: # x mod prime = 0
                    break
        return len(primes)


    def isPrime(self, x):
        import math
        for i in range(2, int(math.sqrt(x))):
            if i ** 2 > x:
                break
            elif x % i == 0:
                return False
        return True



if __name__ == "__main__":
    obj = Solution()
    n = 10
    print(obj.countPrimes(n))