def main(s):
    """
    A string of numbers is given. Find how many even digits there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    a=len(s)
    s=int(s)
    i=0
    c=0
    while i<a:
        if (s%10)%2==0:
            c+=1
        i+=1
        s//=10
    return c
print(main("56786543250"))