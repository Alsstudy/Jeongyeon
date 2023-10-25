from collections import deque

def solution(tickets):
    answer = []
    queue = deque([])
    queue.append((0, "ICN", []))

    tickets.sort(key=lambda x: (x[0], x[1]))

    while queue:
        cnt, start, li = queue.popleft()
        if len(li) == len(tickets):
            for i in li:
                answer.append(tickets[i][0])
            answer.append(tickets[li[-1]][1])
            return answer
        for i in range(len(tickets)):
            if tickets[i][0] == start and i not in li:
                nli = li[:]
                nli.append(i)
                queue.append((cnt+1, tickets[i][1], nli))


print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))
