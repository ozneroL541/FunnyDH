from Crypto.Util import number
import funnydh as fdh

# Number of bits
n = fdh.n
# Generator
g = fdh.g

def main():
    p:int = int(input("Enter the prime number:\t"))
    a:int = int(input("Enter the secret key:\t"))
    B:int = int(input("Enter the other's public key:\t"))
    print()
    
    k = fdh.common_key(a, B, p)

    print(f"Common key:\t{k}")
    k = fdh.humanize(k)
    print(f"Common key:\t{k}")

if __name__ == "__main__":
    main()
