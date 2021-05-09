# https://www.purplefrogsystems.com/blog/2020/03/creating-a-python-function-to-calculate-pi/
# #:~:text=Pi%20is%203.14159%20to%205,7%20%2B%204%2F9%20%E2%80%93%20%E2%80%A6


# def pi():
#     pi = 0
#     n = 4
#     d = 1
#     for i in range (1,10):
#         a = 2 * (i % 2) - 1
#         pi += a * n/d
#         d += 2
#         print(pi)
# pi()

# The pi series will start from 0.
# n represents the numerator of our fractions which is the constant 4.
# d represents the denominator of our fractions which starts as 1.

# d needs to increase by 2 every loop, let’s use sum equals to do this.
# Pi will also use a sum equals, a denotes our positive/negative function which we will get on to:
    

# The only problem left is how to get a to alternate between 1 and -1.
# This is where we introduce modulo.
# Modulo outputs the remainder of a division and is denoted by %.

# However, we are only executing the loop 10 times, hence only 10 terms are being used to calculate Pi.

# Increasing the number of loops to a million will change this:

# def pi():
#     pi = 0
#     n = 4
#     d = 1
#     for i in range (1,1000000):
#         a = 2 * (i % 2) - 1
#         pi += a * n/d
#         d += 2
#         print(pi)
# pi()

#!/usr/bin/env python3

# Find PI to the Nth Digit
# Have the user enter a number 'n'
# and print out PI to the 'n'th digit


def calcPi(limit):  # Generator function
    
    # Prints out the digits of PI
    # until it reaches the given limit1
    q, r, t, k, n, l = 1, 0, 1, 1, 3, 3

    decimal = limit
    counter = 0

    while counter != decimal + 1:
            if 4 * q + r - t < n * t:
                    # yield digit
                    yield n
                    # insert period after first digit
                    if counter == 0:
                            yield '.'
                    # end
                    if decimal == counter:
                            print('')
                            break
                    counter += 1
                    nr = 10 * (r - n * t)
                    n = ((10 * (3 * q + r)) // t) - 10 * n
                    q *= 10
                    r = nr
            else:
                    nr = (2 * q + r) * l
                    nn = (q * (7 * k) + 2 + (r * l)) // (t * l)
                    q *= k
                    t *= l
                    l += 2
                    k += 1
                    n = nn
                    r = nr
def main():  # Wrapper function

    # Calls CalcPi with the given limit
    pi_digits = calcPi(int(input(
        "Enter the number of decimals to calculate to: ")))

    i = 0

    # Prints the output of calcPi generator function
    # Inserts a newline after every 40th number
    for d in pi_digits:
            print(d, end='')
            i += 1
            if i == 40:
                print("")
                i = 0

if __name__ == '__main__':
    main()
    
