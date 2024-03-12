#!/usr/bin/python3
""" Lockboxes """


def canUnlockAll(boxes):
    """ Can unlock all """

    n = len(boxes)
    visited = {}
    for i in range(n):
        visited[i] = 0
    queue = [0]
    visited[0] = 1

    while queue:
        value = queue.pop(0)
        for key in boxes[value]:
            if visited[key] == 0:
                visited[key] = 1
                queue.append(key)

    for (key, value) in visited.items():
        if (value == 0):
            return False
    return True
