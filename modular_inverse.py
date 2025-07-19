

def modular_inverse(a, m):

    # this is the brute-force approach: we check all possible values in the range [0, m-1]
    # problem is that m may be too large ( 1024 bits long prime number )
    # running time seems to be O(m) linear but actually it is exponential as far as
    # the number of input bits are concerned

    for inv in range(0, m):
        if (a * inv) % m == 1:
            return inv
    return -1

    print("There is no modular inverse (a is not a coprime to m) ")    
    pass

if __name__ == "__main__":
    print(modular_inverse(9, 31))