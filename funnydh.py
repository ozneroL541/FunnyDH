from Crypto.Util import number
"""
This module implements a simplified version of the Diffie-Hellman key exchange algorithm.

Functions:
    gen_prime(n: int) -> int:
        Generates a prime number of n bits.
    
    gen_secret_key(p: int) -> int:
        Generates a secret key in the range [2, p-1].
    
    gen_public_key(g: int, p: int, a: int) -> int:
        Generates a public key using the generator g, prime p, and secret key a.
    
    gen_keys(g: int, p: int) -> tuple[int, int]:
        Generates a pair of secret and public keys using the generator g and prime p.
    
    humanize(x: int) -> str:
        Converts an integer to a human-readable string by decoding it as UTF-8.
    
    common_key(a: int, B: int, p: int) -> int:
        Computes the common key using the secret key a, the other party's public key B, and the prime p.
"""

n:int = 256
'''Number of bits for the prime number. '''
g:int = 3
'''Generator for the cyclic group.'''

def gen_prime(n: int) -> int:
    """
    Generate a prime number of n bits.

    Args:
        n (int): The number of bits for the prime number.

    Returns:
        int: A prime number of n bits.
    """
    return number.getPrime(n)

def gen_secret_key(p: int) -> int:
    """
    Generate a secret key for the Diffie-Hellman key exchange.

    Args:
        p (int): A prime number used as the modulus in the Diffie-Hellman key exchange.

    Returns:
        int: A randomly generated secret key in the range [2, p-1].
    """
    return number.getRandomRange(2, p - 1)

def gen_public_key(g, p, a):
    """
    Generate a public key for the Diffie-Hellman key exchange.

    Args:
        g (int): The generator of the cyclic group.
        p (int): A prime number used as the modulus in the Diffie-Hellman key exchange.
        a (int): The secret key.
    
    Returns:
        int: The public key.
    """
    return pow(g, a, p)

def gen_keys(g: int, p: int) -> tuple[int, int]:
    """
    Generate a pair of Diffie-Hellman keys.

    Args:
        g (int): The base (generator) used in the Diffie-Hellman key exchange.
        p (int): The prime modulus used in the Diffie-Hellman key exchange.

    Returns:
        tuple[int, int]: A tuple containing the private key and the corresponding public key.
    """
    a:int = gen_secret_key(p)
    A:int = gen_public_key(g, p, a)
    return a, A

def humanize(x: int) -> str:
    """
    Converts an integer to a human-readable string by encoding it to bytes,
    decoding it to a UTF-8 string, and removing any whitespace characters.

    Args:
        x (int): The integer to be converted.

    Returns:
        str: The human-readable string representation of the integer.
    """
    return ''.join(x.to_bytes((x.bit_length() + 7) // 8, 'big').decode('utf-8', 'ignore').split())

def calc_common_key(a: int, B: int, p: int) -> int:
    """
    Calculate the common key in the Diffie-Hellman key exchange.

    Args:
        a (int): The private key of the first party.
        B (int): The public key of the second party.
        p (int): A prime number used as the modulus.

    Returns:
        int: The computed common key.
    """
    return pow(B, a, p)
