def main(s):
    """
    A variable of type str is given. Find how many uppercase letters there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    a=len(s)
    i=0
    c=0
    while i<a:
        if s[i].isupper():
            c+=1
        i+=1
    return c
print(main("CodeABshLuz"))