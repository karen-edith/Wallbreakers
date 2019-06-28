class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = min(filter(None, strs), key=len, default='')
        commonString = ''
        subCommonString= ''
        subCommonStringArray = []
        count = 0
        unique = []
        cnt = []

        for p in strs:
            if p not in cnt:
                cnt.append(p)

        if len(cnt) == 1:
            return cnt[0]
        if ('' in strs):
            return ''
        elif (len(strs) == 1):
            return strs[0]
        else:
            for j in range (1, len(strs)):
                for k in range (len(prefix)):
                    if (strs[j][k] != prefix[k]):
                        break
                    else:
                        commonString = commonString + prefix[k]

            if len(commonString) == 1:
                return commonString

            else:

                for m in range(len(commonString)):
                    for n in range(len(commonString)):
                        if (commonString[m] == commonString[n]):
                            count = count + 1
                            subCommonString = subCommonString + commonString[m]

                    if len(subCommonString) > 1:
                        subCommonStringArray.append(subCommonString)
                        count = 0
                        subCommonString = ''
                    else:
                        count = 0
                        subCommonString = ''

                for x in subCommonStringArray:
                    if x[0] not in unique:
                        unique.append(x[0])

                return ''.join(unique)
