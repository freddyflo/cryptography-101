

##
def extended_euclidean(a, b):
   
   # base case
   # gcd(0, b) = b and a*x*b*y=b - so x=0 and y=1
    if a == 0:
        return (b, 0, 1)
    

    # euclidean algorithm for gcd()
    # b % a is always the smaller number - and 'a' is the smaller integer
    # always in this implementation
    gcd, x1, y1 = extended_euclidean(b % a, a)


    x = y1 - (b // a) * x1
    y = x1

    return (gcd, x, y)

if __name__ == "__main__":
    print(extended_euclidean(15, 56))