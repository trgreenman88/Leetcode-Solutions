#Runtime: 20 ms, faster than 99.58% of Python online
#submissions for Integer to Roman.

#Memory Usage: 12.7 MB, less than 59.63% of Python online
#submissions for Integer to Roman.

def intToRoman(self, num):
    """
    :type num: int
    :rtype: str
    """
    rnum = ""
        
    if num >= 900:
        while num >= 1000:
            rnum += "M"
            num -= 1000
        if num >= 900:
            rnum += "CM"
            num -= 900

    if num >= 400:
        if num >= 500:
            rnum += "D"
            num -= 500
        if num >= 400:
            rnum += "CD"
            num -= 400

    if num >= 90:
        while num >= 100:
            rnum += "C"
            num -= 100
        if num >= 90:
            rnum += "XC"
            num -= 90

    if num >= 40:
        if num >= 50:
            rnum += "L"
            num -= 50
        if num >= 40:
            rnum += "XL"
            num -= 40

    if num >= 9:
        while num >= 10:
            rnum += "X"
            num -= 10
        if num == 9:
            rnum += "IX"
            return rnum

    if num >= 4:
        if num >= 5:
            rnum += "V"
            num -= 5
        if num == 4:
            rnum += "IV"
            return rnum

    if num >= 1:
        while num >= 1:
            rnum += "I"
            num -= 1
                
    return rnum



