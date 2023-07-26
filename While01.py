def main(s):
    """
    A variable of type str is given. Find how many digits it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    m=len(s)
    i=0
    a=0
    while i<m:
        if s[i].isdigit()==1:
            a+=1
        i+=1
    return a
print(main("pytho1243n"))