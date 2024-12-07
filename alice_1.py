from Crypto.Util import number
import funnydh as fdh

n:int = fdh.n
'''Number of bits for the prime number. '''
g:int = fdh.g
'''Generator for the cyclic group.'''

def main():
    """
    Main function to generate Diffie-Hellman key pairs and print the configuration.

    This function performs the following steps:
    1. Generates a prime number `p` using the `fdh.gen_prime` function.
    2. Generates a private key `a` and a public key `A` using the `fdh.gen_keys` function with generator `g` and prime `p`.
    3. Prints the configuration details including the generator, number of bits, prime number, public key, and secret key.

    Note:
        - `fdh` is assumed to be a module that provides the `gen_prime` and `gen_keys` functions.
        - `g` and `n` are assumed to be predefined variables representing the generator and the number of bits, respectively.
    """
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

if __name__ == "__main__":
    main()
