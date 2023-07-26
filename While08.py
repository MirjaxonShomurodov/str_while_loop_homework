def main(s):
    """
    A string of numbers is given. Find how many odd digits there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    a=len(s)
    s=int(s)
    i=0
    toq=0
    while i<a:
        if (s%10)%2==1:
            toq+=1
        i+=1
        s//=10
    return toq
print(main("1234567890"))