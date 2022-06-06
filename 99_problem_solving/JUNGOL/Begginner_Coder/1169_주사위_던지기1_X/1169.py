import sys

input = sys.stdin.readline

N, M = map(int, input().strip().split())

# 2번에서 쓸 것
num_list = [1] * N

my_set = []



def do1(i):
    if i == N:
        print(*num_list)
    else:
        while num_list[i] < 7:
            do1(i + 1)
            num_list[i] += 1
        num_list[i] = 1

def do2(i):
    if i == N:
        C = [0] * 7
        for i in range(N):
            C[num_list[i]] += 1
        if C in my_set:
            return
        else:
            print(*num_list)
            my_set.append(C)
    else:
        while num_list[i] < 7:
            do2(i + 1)
            num_list[i] += 1
        num_list[i] = 1

# 3번에서 쓸 것
visited = [0] * 7
N_list = [0] * N
def do3(i):
    if i == N:
        print(visited)
    else:
        for j in range(1, 7):
            if not visited[j]:
                visited[j] = 1
                N_list[i] = j
                do3(i+1)


if M == 1:
    do1(0)
elif M == 2:
    do2(0)
elif M == 3:
    do3(0)