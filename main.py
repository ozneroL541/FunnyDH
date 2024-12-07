import alice_1 as a1
import bob as b
import alice_2 as a2

def main():
    print("A1\t- Alice 1")
    print("B\t- Bob")
    print("A2\t- Alice 2")
    print()
    option = input("Option:\t")

    if "B" in option:
        b.main()
    elif option == "A2":
        a2.main()
    elif "A" in option and "2" in option:
        a2.main()
    elif "A" in option:
        a1.main()
    else:
        print("Invalid option")


if __name__ == "__main__":
    main()
