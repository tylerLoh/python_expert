T = int(input())

for t in range(T):
    N, M, Q = map(int, input().split())
    P = map(int, input().split())
    R = list(map(int, input().split()))

    good_pages = [True] * (N + 1)
    for p in P:
        good_pages[p] = False

    prev = {}
    total = 0

    for r in R:
        if r in prev.keys():
            total += prev[r]
            continue

        count = 0
        for i in range(r, N + 1, r):
            if good_pages[i]:
                count += 1
        prev[r] = count
        total += count
    print(f"Case #{t+1}: {total}")

