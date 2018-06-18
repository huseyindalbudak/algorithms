'''
def combination(n, r):
    # This function calculates nCr
    if n == r or r == 0:
        return 1
    else:
        return combination(n-1, r-1) + combination(n-1, r)
'''
 # the code so fast according to old code, such as combination(50,10)
 def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def combination(n,r):
    return factorial(n) /factorial(r) / factorial(n-r)
