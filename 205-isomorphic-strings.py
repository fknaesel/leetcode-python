"""
205. Isomorphic Strings

Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while 
preserving the order of characters. No two characters may map to the same 
character, but a character may map to itself.

Example 1: Input: s = "egg"  , t = "add"     Output: true
Example 3: Input: s = "paper", t = "title"   Output: true
Example 2: Input: s = "foo"  , t = "bar"     Output: false
Example 4: Input: s = "bacd" , t = "baba"    Output: false

Constraints:
    1 <= s.length <= 5 * 10^4
    t.length == s.length
    s and t consist of any valid ascii character.
"""

from typing import List

class Solution:
    # def isIsomorphicSlow(self, s: str, t: str) -> bool:
    #     fro = ""
    #     too = ""
    #     new = ""
    #     for i in range(len(s)):
    #         found = False
    #         for tt in too:
    #             if t[i] == tt:
    #                 found = True
    #                 break
    #         if not found:
    #             fro += s[i]
    #             too += t[i]

    #     print(f"fro={fro} -> too={too}")        

    #     for i in range(len(t)):
    #         try:
    #             new += too[fro.index(s[i])]
    #         except:
    #             print(f"t={t} s={s} Non-Isomorphic")
    #             return False
        
    #     if t == new:
    #         print(f"t={t} s={s} Isomorphic")
    #         return True
    #     else:
    #         print(f"t={t} s={s} Non-Isomorphic")
    #         return False
        
    # def isIsomorphic(self, s: str, t: str) -> bool:
    #     if len(s) != len(t):
    #         return False
        
    #     fro = ""
    #     too = ""
    #     for i in range(len(s)):
    #         found = False
    #         index = -1
    #         ti = t[i]
    #         si = s[i]
    #         for j in range(len(too)):
    #             if t[i] == fro[j]:
    #                 found = True
    #                 index = j
    #                 break
    #             if s[i] == too[j]:
    #                 print(f"s={s} t={t}   fro={fro} too={too}   False")
    #                 return False
                
    #         if not found:
    #             fro += t[i]
    #             too += s[i]
    #         else:
    #             if si != too[index]:
    #                 print(f"s={s} t={t}   fro={fro} too={too}   False")
    #                 return False
        
    #    print(f"s={s} t={t}   fro={fro} too={too}   True")
    #    return True

    def isIsomorphic(self, s: str, t: str) -> bool:
        d = {}
        for i in range(len(t)):

            if t[i] in d:
                if d[t[i]] != s[i]:
                    # print(f"s={s} t={t}      False")
                    return False
            else:
                if s[i] in d.values():
                    # print(f"s={s} t={t}      False")
                    return False
                else:
                    d[t[i]] = s[i]
            # print(d)

        # print(f"s={s} t={t}      True")
        return True


s = Solution()
s.isIsomorphic(s="egg", t="add") # Output: True
s.isIsomorphic(s="foo", t="bar") # Output: False
s.isIsomorphic(s="badc", t="baba") # Output: False
s.isIsomorphic(s="paper", t="title") # Output: True
