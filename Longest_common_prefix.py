class Solution:
    def longestCommonPrefix(self, strs):
        common = ''
        result = ''

        for item in strs:
            if len(item) == 0:
                break

        if len(strs) == 1:
            common = strs[0]
        elif strs[0] == '' or strs[1] == '':
                common = ''
        else:
            q = 1
            for j in range(min(len(strs[0]),len(strs[1]))):
                if strs[0][j] == strs[1][j] and q == 1:
                    common += strs[0][j]
                elif strs[0][j] != strs[1][j]:
                    q *= 0 
            print(common)
            strs.pop(0)
            strs.pop(0)
            if len(common) > 0:
                for item in strs:
                    if len(item) == 0:
                        common  = ''
                    else:
                        print('next length  ' + str(min(len(common),len(item)))+item)
                        if min(len(common),len(item)) == 1:
                            if common[0] == item[0]:
                                common = common[0]
                            else:
                                common = ''
                        else:
                            for j in range(min(len(common),len(item))):
                                commonLH = common[:j]
                                if common[j] != item[j]:
                                    print(j)
                                    common = common[:j]
                                    break
        result = common

        return result
        
            
        
