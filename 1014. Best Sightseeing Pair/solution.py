'''Intuition:
Count the current best score in all previous sightseeing spot.
Note that, as we go further, the score of previous spot decrement.

Explanation
cur will record the best score that we have met.
We iterate each value a in the array A,
update res by max(res, cur + a)

Also we can update cur by max(cur, a).
Note that when we move forward,
all sightseeing spot we have seen will be 1 distance further.

So for the next sightseeing spot cur = Math.max(cur, a) **- 1**

It's kinds of like, "A near neighbor is better than a distant cousin."

Time Complexity:
One pass, O(N) time, O(1) space

'''
def maxScoreSightseeingPair(self, A):
        cur = res = 0
        for a in A:
            res = max(res, cur + a)
            cur = max(cur, a) - 1
        return res

def maxScoreSightseeingPair(self, A):
        return reduce(lambda (r, c), a: [max(r, c + a), max(c, a) - 1], A, [0, 0])[0]