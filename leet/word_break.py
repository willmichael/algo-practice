class Solution(object):
    # def wordBreak(self, s, words):
        # ok = [True]
        # for i in range(1, len(s)+1):
            # print any(ok[j] and s[j:i] in words for j in range(i)), 'hi'
            # ok += any(ok[j] and s[j:i] in words for j in range(i)),
        # return ok[-1]

    def wordBreak(self, s, words):
        ok = [True]
        print len(s)
        for i in range(1, len(s)+1):
            # ok += any(ok[j] and s[j:i] in words for j in range(i)),
            # print ok
            res = []
            for j in range(i):
                # ok += any(ok[j] and s[j:i] in words for j in range(i)),
                res += [ok[j] and (s[j:i] in words)]
                print res, 'what'
                
                # print s[j:i]
                # print any(ok[j] and (s[j:i] in words))
                # if s[j:i] in words:
                    # print s[j:i]
                # ok += any(ok[j] and s[j:i] in words)
        print ok
        return ok[-1]



s = "leetcode"
words = ["code", "le", "et"]

so = Solution()
print so.wordBreak(s, words)
    # def wordBreak(self, s, wordDict):
        # """
        # :type s: str
        # :type wordDict: List[str]
        # :rtype: bool
        # """
        
        # if s == '':
            # return True
        # for i in range(s):
            # if s[0:i] in wordDict:
                

