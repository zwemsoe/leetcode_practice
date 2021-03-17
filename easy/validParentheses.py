import sys
import math

def isValid(self, s: str) -> bool:
        a = [s[0]]
        for i in range(1, len(s)):
            if len(a):
                if a[len(a)-1] == '(' and s[i] == ')':
                    a.pop()
                elif a[len(a)-1] == '[' and s[i] == ']':
                    a.pop()
                elif a[len(a)-1] == '{' and s[i] == '}':
                    a.pop()
                else:
                    a.append(s[i])
            else:
                a.append(s[i])
                
        return True if len(a) == 0 else False
