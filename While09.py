def main(s):
    """
    A string of numbers is given. Find the sum of all the digits and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
   
    s=int(s)
    i=0
    while 0<s:
        i += (s%10)
        s//=10
    return i
print(main("1843"))