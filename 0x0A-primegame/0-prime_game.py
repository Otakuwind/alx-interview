#!/usr/bin/python3
"""Module defining isWinner function."""


def isWinner(x, nums):
    def isPrime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def canWin(n):
        dp = [False] * (n + 1)
        dp[0] = False
        dp[1] = False

        for i in range(2, n + 1):
            if isPrime(i):
                dp[i] = True
                continue
            for j in range(2, i // 2 + 1):
                if i % j == 0 and not dp[i - j]:
                    dp[i] = True
                    break

        return dp[n]

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if canWin(n):
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

# Example usage:
x = 3
nums = [4, 5, 1]
result = isWinner(x, nums)
print(result)  # Output: "Ben"

