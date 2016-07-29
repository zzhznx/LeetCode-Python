class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        primes = [True] * n
        primes[:2] = [False, False]
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                primes[i * i : n : i] = [False] * len(primes[i * i : n : i])
        return sum(primes[:])

solution = Solution()
print(solution.countPrimes(3))
print(solution.countPrimes(150))