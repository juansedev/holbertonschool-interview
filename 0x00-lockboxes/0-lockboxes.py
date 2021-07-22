#!/usr/bin/python3
"""
Module of canUnlockAll
"""

def canUnlockAll(boxes):
    """ validate if all the boxes can be opened
    """
    opened = [0]
    if (len(boxes) == 0):
        return True
    for i in opened:
        for i_box in boxes[i]:
            if i_box not in opened:
                if i_box < len(boxes):
                    opened.append(i_box)
    if len(opened) == len(boxes):
        return True
    return False