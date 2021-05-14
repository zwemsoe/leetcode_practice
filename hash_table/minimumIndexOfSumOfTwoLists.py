import sys
import math


def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
    hashMap = {}
    i = j = 0
    for w in list1:
        hashMap[w] = i
        i += 1

    temp = {}
    for w in list2:
        if (w in hashMap):
            temp[w] = hashMap[w]+j
        j += 1

    minVal = min(temp.values())

    return [k for k, v in temp.items() if v == minVal]
