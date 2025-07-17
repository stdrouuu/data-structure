#polynomial 
#P(x) = a0 + a1x + a2x^2 + ... + anX^n
#polynomial untuk menjumlahkan persamaan

import array as arr 

def create_poly(poly):
    while True:
        cof = int(input("Enter Coefficient: "))
        pwr = int(input("Enter Power: "))
        poly[pwr] = cof
        ch = input("Continue? (y/n): ")
        if ch.upper() == "N":
            break

def display_poly(poly):
    size = len(poly)
    for i in range(size-1, -1, -1):
        if poly[i] != 0:
            print(str(poly[i]) + "x^" + str(i), end = "+")
    print("\b")

def add_poly(poly1, poly2):
    ln = len(poly1)
    poly3 = arr.array('i', [0] * ln)
    for i in range(ln):
        poly3[i] = poly1[i] + poly2[i]
    return poly3

p1 = int(input("Enter the highest power of 1st polynomial: "))
p2 = int(input("Enter the highest power of 2nd polynomial: "))
p = max(p1, p2)
poly1 = arr.array('i', [0] * (p + 1))
poly2 = arr.array('i', [0] * (p + 1))
print("Enter value for 1st polynomial: ")
create_poly(poly1)
print("Enter value for 2nd polynomial: ")
create_poly(poly2)
poly3 = add_poly(poly1, poly2)
print("\n1st Polynomial: ", end = "")
display_poly(poly1)
print("\n2nd Polynomial: ", end = "")
display_poly(poly2)
print("\nResult Polynomial: ", end = "")
display_poly(poly3)

#polynomial 
#P(x) = a0 + a1x + a2x^2 + ... + anX^n
#polynomial untuk menjumlahkan persamaan

#Poly1 = 1 + 2x^1 - 3x^2
#Poly2 = 0  + 0x^0 + 0x^0 + 6x^3 + 4x^4 + 8x^5