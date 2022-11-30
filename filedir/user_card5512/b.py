def shuffle():
    lst = [0] * n
    for i in range(n):
        lst[S[i]] = card[i]
    return lst


def check():
    for i in range(n):
        if P[i] != card.index(i) % 3:
            return False
    return True


n = int(input())
P = list(map(int, input().split()))
S = list(map(int, input().split()))
card = list(range(n))
start = card

cnt = 0
while not check():
    card = shuffle()
    if card == start:
        print(-1)
        break
    cnt += 1
else:
    print(cnt)
