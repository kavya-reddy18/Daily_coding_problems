# using hashing
def solve(a, n, k):
    d = dict()
    for i in range(n):
        curr = k - a[i]
        if curr in d:
            return True
        if a[i] in d:
            d[a[i]] += 1
        else:
            d[a[i]] = 1
    return False
# using two pointer approach
def solve1(a, n, k):
    a.sort()
    p1 = 0
    p2 = n - 1
    while (p1 <= p2):
        temp = a[p1] + a[p2]
        if temp < k:
            p1 += 1
        elif temp > k:
            p2 -= 1
        else:
            return True
    return False
# using binary search
def solve2(a, n, k):
    a.sort()
    for i in range(n):
        k1 = k - a[i]
        low = i + 1
        high = n - 1
        while (low <= high):
            mid = (low + high) // 2
            if a[mid] == k1:
                return True
            elif a[mid] > k1:
                high = mid - 1
            else:
                low = mid + 1
    return False
n, k = map(int, input().split())
a = list(map(int, input().split()))
print(solve2(a, n, k))