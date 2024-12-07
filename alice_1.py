from Crypto.Util import number
import funnydh as fdh

# Number of bits
n = fdh.n
# Generator
g = fdh.g

def main():
    p = fdh.gen_prime(n)
    a, A = fdh.gen_keys(g, p)

    print("Configuration")
    print(f"Generator:\t{g}")
    print(f"Number of bits:\t{n}")
    print("-" * 55)
    print(f"Prime number:\t{p}")
    print(f"Public key:\t{A}")
    print()
    print(f"Secret key:\t{a}")

if __name__ == "__main__":
    main()
