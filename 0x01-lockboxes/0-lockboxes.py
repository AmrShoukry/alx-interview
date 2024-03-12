#!/usr/bin/python3
""" Lockboxes """

def canUnlockAll(boxes):
    """ Can unlock all """
    
    n = len(boxes)
    set = {}
    for i in range(n):
        set[i] = 0;
    queue = [0]
    set[0] = 1
    
    while queue:
        value = queue.pop(0)
        for key in boxes[value]:
            if set[key] == 0:
                set[key] = 1
                queue.append(key)
                
    for (key, value) in set.items():
        if (value == 0):
            return False
    return True
    