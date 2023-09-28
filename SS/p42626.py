import heapq

def solution(scoville, K):
    answer = 0
    length = len(scoville)

    heap = []
    for num in scoville:
        heapq.heappush(heap, num)

    while True:
        if all(K <= s for s in heap):
            return answer
        if length < 2:
            return -1
        answer += 1
        heapq.heappush(heap, heapq.heappop(heap) + heapq.heappop(heap) * 2)
        length -= 1


print(solution([1, 2, 3, 9, 10, 12], 7))