from Crypto.Util import number

# Number of bits
n = 128
# Generator
g = 3

def gen_prime(n:int) -> int:
    return number.getPrime(n)

def gen_secret_key(p: int) -> int:
    return number.getRandomRange(2, p - 1)

def gen_public_key(g, p, a):
    return pow(g, a, p)

def gen_keys(g: int, p: int) -> tuple[int, int]:
    a = gen_secret_key(p)
    A = gen_public_key(g, p, a)
    return a, A

def humanize(x: int) -> str:
    return ''.join(x.to_bytes((x.bit_length() + 7) // 8, 'big').decode('utf-8', 'ignore').split())

def common_key(a: int, B: int, p: int) -> int:
    return pow(B, a, p)
