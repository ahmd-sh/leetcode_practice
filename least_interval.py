def leastInterval(tasks: List[str], n: int) -> int:
    time = 0
    count = Counter(tasks)

    max_heap = [-c for c in count.values()]
    heapq.heapify(max_heap)
    q = deque()

    while max_heap or q:
        time += 1

        # Optimization:
        # if not max_heap:
        #     time = q[0][1]
        # else:

        if max_heap:
            left = heapq.heappop(max_heap) + 1
            if left:
                q.append([left, time + n])

        if q and q[0][1] == time:
            heapq.heappush(max_heap, q.popleft()[0])

    return time
