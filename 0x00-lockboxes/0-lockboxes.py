#!/usr/bin/python3
"""
    Module of canUnlockAll
"""

def canUnlockAll(boxes):
    """ validate if all the boxes can be opened
    """
    arr = [0]
    if (len(boxes) == 0):
        return True
    for i in arr:
        for i_box in boxes[i]:
            if i_box not in arr:
                if i_box < len(boxes):
                    arr.append(i_box)
    if len(arr) == len(boxes):
        return True
    return False
