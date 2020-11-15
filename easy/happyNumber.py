import sys
import math


def isHappy(self, n: int) -> bool:
    seen = {}
    seen[n] = n
    while True:
        t = n
        sm = 0
        while t != 0:
            sm += (t % 10)**2
            t = int(t/10)
        if sm == 1:
            return True
        else:
            if sm in seen:
                return False
            else:
                seen[sm] = sm
                n = sm


def main():
    pass


main()
