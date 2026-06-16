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
        
        minHeap = []
        users = self.following[userId].copy()
        users.add(userId)

        for user in users:
            for time, tweetId in self.tweets[user]:
                heapq.heappush(minHeap, (time, tweetId))

                if len(minHeap) > 10:
                    heapq.heappop(minHeap)
        
        res = []
        while minHeap:
            time, tweetId = heapq.heappop(minHeap)
            res.append(tweetId)

        return res[::-1]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)

    
