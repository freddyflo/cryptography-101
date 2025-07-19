
# Greatest Common Divisor (GCD)
def gcd(a, b):

    # base-case: if b|a (without a remainder) then b is tge gcd
    if a % b == 0:
        return b
    
    return gcd(b, a % b)

def gcd_iterative(a, b):
    
    while a % b != 0:
        a, b = b, a % b
    
    return b


if __name__ == "__main__":
    print(gcd_iterative(24, 9))