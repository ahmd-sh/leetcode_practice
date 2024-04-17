class Twitter:

    def __init__(self):
        self.tweet_index = 0
        self.following_map = defaultdict(set)
        self.tweet_map = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_map[userId].append([self.tweet_index, tweetId])
        self.tweet_index -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        min_heap = []
        self.following_map[userId].add(userId)

        for followeeId in self.following_map[userId]:
            if followeeId in self.tweet_map:
                index = len(self.tweet_map[followeeId]) - 1
                tweet_index, tweetId = self.tweet_map[followeeId][index]
                min_heap.append([tweet_index, tweetId, followeeId, index-1])

        heapq.heapify(min_heap)

        while min_heap and len(res) < 10:
            tweet_index, tweetId, followeeId, index = heapq.heappop(min_heap)
            res.append(tweetId)
            if index >= 0:
                tweet_index, tweetId = self.tweet_map[followeeId][index]
                heapq.heappush(min_heap, [tweet_index, tweetId, followeeId, index-1])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following_map[followerId]:
            self.following_map[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
