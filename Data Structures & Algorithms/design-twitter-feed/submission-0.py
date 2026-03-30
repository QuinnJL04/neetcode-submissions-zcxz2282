import heapq

class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)
        
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1


    def getNewsFeed(self, userId: int) -> List[int]:
        h = []
        heapq.heapify(h)
        res = []

        # Always follow self
        self.following[userId].add(userId)

        for followeeId in self.following[userId]:
            if followeeId in self.tweets:
                index = len(self.tweets[followeeId]) - 1
                count, tweetId = self.tweets[followeeId][index]
                heapq.heappush(h, [-count, tweetId, followeeId, index - 1])  # Use -count for max-heap behavior

        while h and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(h)
            res.append(tweetId)
            if index >= 0:
                count2, tweetId2 = self.tweets[followeeId][index]
                heapq.heappush(h, [-count2, tweetId2, followeeId, index - 1])

        return res



    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].discard(followeeId)
