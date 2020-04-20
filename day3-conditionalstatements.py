'''Task
Given an integer, n, perform the following conditional actions:

If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5, print Not Weird
If n is even and in the inclusive range of 6 to 20, print Weird
If n is even and greater than 20, print Not Weird
Complete the stub code provided in your editor to print whether or not n is weird.'''

#!/bin/python3

if __name__ == '__main__':
    N = int(input())
    print("Weird" if ((N%2!=0) or (N%2==0 and N in range(6,21))) else "Not Weird")
