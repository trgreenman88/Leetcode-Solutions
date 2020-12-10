#Runtime: 20 ms, faster than 18.93% of Python online
#submissions for Roman to Integer.

#Memory Usage: 12.7 MB, less than 51.93% of Python online
#submissions for Roman to Integer.

def romanToInt(s):
        
        total = 0
        templist = []
        for i in range(len(s)):
            templist.append(s[i])
            if i > 0:
                current = templist[i]
                previous = templist[i-1]
                if (current == "V" or current == "X") and (previous == "I"):
                    total -= 2
                if (current == "L" or current == "C") and (previous == "X"):
                    total -= 20
                if (current == "D" or current == "M") and (previous == "C"):
                    total -= 200   
        
        for i in templist:
            if i == "I":
                total += 1
            elif i == "V":
                total += 5
            elif i == "X":
                total += 10
            elif i == "L":
                total += 50
            elif i == "C":
                total += 100
            elif i == "D":
                total += 500
            elif i == "M":
                total += 1000
                
            
            
        return total

print(romanToInt("MCMXCIV"))
            
