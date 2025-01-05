from Crypto.Util import number
import funnydh as fdh

n:int = fdh.n
'''Number of bits for the prime number. '''
g:int = fdh.g
'''Generator for the cyclic group.'''

def main():
    """
    Main function to perform the Funny Diffie-Hellman key exchange.

    Prompts the user to input a prime number, a secret key, and the other's public key.
    Calculates the common key using the provided inputs and prints it.
    Then, humanizes the common key and prints it again.

    Inputs:
        p (int): The prime number.
        a (int): The secret key.
        B (int): The other's public key.
    Outputs:
        Prints the common key and the humanized common key.
    """
    p:int = int(input("Enter the prime number:\t"))
    a:int = int(input("Enter your secret key:\t"))
    B:int = int(input("Enter Bob's public key:\t"))
    k:int = fdh.calc_common_key(a, B, p)
    print("-" * 55)
    print(f"Common key:\t{k}")
    k:str = fdh.humanize(k)
    print(f"Common key:\t{k}")

if __name__ == "__main__":
    main()
