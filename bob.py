import funnydh as fdh

# Number of bits
n = fdh.n
# Generator
g = fdh.g

def main():
    """
    Main function to execute the Funny Diffie-Hellman key exchange for Bob.

    Prompts the user to input a prime number and a public key, then generates Bob's private and public keys,
    calculates the common key, and prints the generator, Bob's public key, and the common key in both raw and human-readable formats.

    Inputs:
        - Prime number (p): An integer representing the prime number used in the Diffie-Hellman key exchange.
        - Public key (A): An integer representing Alice's public key.

    Outputs:
        - Prints the generator value.
        - Prints Bob's public key.
        - Prints the common key in both raw and human-readable formats.
    """
    p:int = int(input("Enter the prime number:\t"))
    A:int = int(input("Enter the public key:\t"))

    b, B = fdh.gen_keys(g, p)
    k = fdh.calc_common_key(b, A, p)

    print(f"Generator:\t\t{g}")
    print("-" * 50)
    print(f"Public key:\t{B}")
    print()
    print(f"Common key:\t{k}")
    k = fdh.humanize(k)
    print(f"Common key:\t{k}")

if __name__ == "__main__":
    main()
