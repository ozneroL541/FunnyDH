import funnydh as fdh

n:int = fdh.n
'''Number of bits for the prime number. '''
g:int = fdh.g
'''Generator for the cyclic group.'''

def main():
    p:int = fdh.gen_prime(n)
    a, A = fdh.gen_keys(g, p)

    print("Configuration")
    print(f"Generator:\t{g}")
    print(f"Number of bits:\t{n}")
    print("-" * 55)
    print(f"Prime number:\t{p}")
    print(f"Public key:\t{A}")
    print()
    print(f"Secret key:\t{a}")
    B:int = int(input("Enter Bob's public key:\t"))
    k:int = fdh.calc_common_key(a, B, p)
    print("-" * 55)
    print(f"Common key:\t{k}")
    k:str = fdh.humanize(k)
    print(f"Common key:\t{k}")

if __name__ == "__main__":
    main()
