def solution(upSpeed, downSpeed, desiredHeight):
    return 1 if upSpeed >= desiredHeight else math.ceil((desiredHeight - upSpeed) / (upSpeed - downSpeed) + 1)
