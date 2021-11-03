class Solution:
    def romanToInt(self, s):
        number = []
        for roman in s:
            if roman == 'I':
                number.append(1)
            elif roman == 'V':
                number.append(5)
            elif roman =='X':
                number.append(10)
            elif roman == 'L':
                number.append(50)
            elif roman == 'C':
                number.append(100)
            elif roman == 'D':
                number.append(500)
            else:
                number.append(1000)
        print(number)
        integer = number[-1]
            
        for i in range(0,len(number)-1):
            if number[i+1] > number[i]:
                j = -1
            else:
                j = 1
            integer += j* number[i]
            
        return integer
        
