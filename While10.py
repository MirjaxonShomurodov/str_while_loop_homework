def main(s):
    """
    A string of numbers is given. Find and return the sum of all odd digits.
    Args:
        s: str
    Returns:
        int: return answer
    """
    s=int(s)
    i=0
    a=0
    while 0<s:
        if ((s%10)%2==1):
            a+=s%10 
        s//=10
    return a
print(main("9532413"))