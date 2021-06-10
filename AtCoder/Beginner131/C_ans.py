def gcd(c, d):
    if (d == 0): return c
    else: return gcd(d, c % d)

def f(n, c, d):
    return n - (n // c + n // d - n // (c * d // gcd(c, d)))

def main():
    a,b,c,d = map(int, input().split())
    print (f(b, c, d) - f(a - 1, c, d))

if __name__ == "__main__":
    main()