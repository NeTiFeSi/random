def solution(votes, k):
    m = max(votes) - k
    return sum(v > m for v in votes) if k != 0 else 1 if votes.count(m) == 1 else 0
