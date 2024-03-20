def k_closest(points, k):
    # Hashmap method
    # hm = defaultdict(list)

    # for p in points:
    #     distance = p[0]**2 + p[1]**2
    #     hm[distance].append(p)

    # hm_s = sorted(hm.items(), key=lambda x: x[0])[:k]

    # flat_lists = []
    # for _, points_list in hm_s:
    #     flat_lists.extend(points_list)
    
    # return [list(item) for item in flat_lists][:k]

    # Heap method
    res = []
    min_heap = []

    for x, y in points:
        distance = x**2 + y**2
        min_heap.append((distance, x, y))

    heapq.heapify(min_heap)

    for _ in range(k):
        _, x, y = heapq.heappop(min_heap)
        res.append((x, y))

    return res
