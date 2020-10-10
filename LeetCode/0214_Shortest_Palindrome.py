class Solution(object):
    def shortestPalindrome(self, s):
        a = s+"*"+s[::-1]
        lps = self.getLPS(a)
        return s[lps[-1]:][::-1] + s

    def getLPS(self, pattern): 
        m = len(pattern)
        lps = [0] * m
        i, j = 0, 1

        while j < m: 
            if pattern[i] == pattern[j]: 
                lps[j] = i + 1
                i, j = i+1, j+1
            elif i != 0:
                i = lps[i - 1]
            else:
                lps[j] = 0
                j += 1
        return lps
