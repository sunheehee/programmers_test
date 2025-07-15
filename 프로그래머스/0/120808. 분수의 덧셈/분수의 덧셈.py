import math #기약분수를 만들기 위해 최대공약수로 분수를 나누기 위함
def solution (numer1, denom1, numer2, denom2):
    numer = numer1 * denom2 + numer2 * denom1
    denom = denom1 * denom2 
    gcd = math.gcd(numer,denom)
    
    return [numer//gcd, denom//gcd]