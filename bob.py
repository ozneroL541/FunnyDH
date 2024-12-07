import funnydh as fdh

# Number of bits
n = fdh.n
# Generator
g = fdh.g

def main():
    p:int = int(input("Enter the prime number:\t"))
    A:int = int(input("Enter the public key:\t"))

    b, B = fdh.gen_keys(g, p)
    k = fdh.common_key(b, A, p)

    print(f"Generator:\t\t{g}")
    print("-" * 50)
    print(f"Public key:\t{B}")
    print()
    print(f"Common key:\t{k}")
    k = fdh.humanize(k)
    print(f"Common key:\t{k}")

if __name__ == "__main__":
    main()
