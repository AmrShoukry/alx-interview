#!/usr/bin/python3
""" Lockboxes """


def canUnlockAll(boxes):
    """ canUnlockAll """
    availableList = [0]
    completed = []

    while len(availableList) != 0:
        avaialbleElement = availableList[0]
        for element in boxes[avaialbleElement]:
            if (element not in availableList and element not in completed):
                availableList.append(element)
        completed.append(avaialbleElement)
        availableList.pop(0)

    if (len(completed) == len(boxes)):
        return True
    return False
