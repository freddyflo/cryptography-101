import random

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return str(self.x) + " " + str(self.y)
        pass
  
class EllipticCurveCryptography:

    # y^2 = x^3 + ax + b
    def __init__(self, a, b):
        self.a = a
        self.b = b
        pass

    def point_addition(self, p, q):
        
        x1, y1 = p.x, p.y
        x2, y2 = q.x, q.y

        if x1 == x2 and y1 == y2:
            # point doubling operation 
            m = (3 * x1**2 + self.a) / (2 * y1)
        else:
            # point addition operation (p !=q )
            m = ( y2 - y1 ) / ( x2 - x1 )

        # we have update x3 and y3 coordinates
        x3 = m*m - x1 - x2
        y3 = m*(x1 - x3) - y1

        return Point(x3, y3)
    
    # O(m) linear running time complexity
    def double_and_add(self, n, p):

        temp_point = Point(p.x, p.y)
        binary = bin(n)[3:]
        
        for binary_char in binary:
            # print doubling operation
            temp_point = self.point_addition(temp_point, temp_point)

            if binary_char == '1':
                # print addition operation
                temp_point = self.point_addition(temp_point, p)

        return temp_point
    
if __name__ == "__main__":

        ecc = EllipticCurveCryptography(0, 7)
        # point = Point(1, 1)
        # print(ecc.point_addition(point, point))

        # E elliptic curve + G generator is public 
        generator_point = Point(-2, -1)

        # Alice random number (a)
        alice_random = random.randint(2, 10000)

        # Bob's random number (b)
        bob_random = random.randint(2, 10000)

        # public key with double and add algorithm
        alice_public = ecc.double_and_add(alice_random, generator_point)
        bob_public = ecc.double_and_add(bob_random, generator_point)

        # generate the private key
        alice_secret_key = ecc.double_and_add(alice_random, bob_public)
        bob_secret_key = ecc.double_and_add(bob_random, alice_public)
        
        print(alice_secret_key)
        