# baekjoonk
from collections import deque
input_data = list(map(int, input().split()))

print(list(input_data))
n = input_data[0]
m = input_data[1]
k = input_data[2]
x = input_data[3]

print(n, m, k, x)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)

distance = [-1]*(n+1)
distance[x] = 0
q = deque([x])
while q:
    now = q.popleft()
    for next in graph[now]:
        if distance[next] ==-1:
            distance[next] = distance[now] +1
            q.append(next)

    check = False
    for  i in range(1, n +1):
        if distance[i] == k:
            print[i]
            check = True
    if check == False:
        print(-1)

