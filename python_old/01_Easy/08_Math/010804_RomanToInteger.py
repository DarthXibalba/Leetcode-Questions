# Approach 1: Intuitive Left -> Right approach with a mapping of single & double char Roman Numerals
def romanToInt_1(s):
    """
    :type s: str
    :rtype: int
    """
    rToI = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    rToI_Pairs = {
        "IV": 4,
        "IX": 9,
        "XL": 40,
        "XC": 90,
        "CD": 400,
        "CM": 900
    }
    sum = 0
    i = 0
    while (i < len(s)):
        # Query = pair of roman numerals
        q = s[i:i+2]
        if q in rToI_Pairs:
            print(f"q2 = {q}")
            sum += rToI_Pairs[q]
            i += 2
        # It must be a single character roman numeral
        else:
            print(f"q1 = {s[i]}")
            sum += rToI[s[i]]
            i += 1
    return sum

# Appraoch 2: Right -> Left Additive/Subtractive Approach
def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    rToI = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    i = len(s) - 1
    sum = rToI[s[i]]
    i -= 1
    while (i >= 0):
        # If previous is greater than current, then subtract the two numbers
        if rToI[s[i+1]] > rToI[s[i]]:
            sum -= rToI[s[i]]
        else:
            sum += rToI[s[i]]
        i -= 1
    return sum


if __name__ == '__main__':
    nums = [
        "III",
        "LVIII",
        "MCMXCIV"
    ]
    answers = [
        3,
        58,
        1994
    ]
    for i in range(len(nums)):
        ans = romanToInt(nums[i])
        print(f"Roman Numeral = {nums[i]}")
        print(f"Integer Representation = {ans}")
        assert answers[i] == ans, f"{answers[i]} != {ans}"
        print("")