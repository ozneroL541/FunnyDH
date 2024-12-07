import alice_1 as a1
import bob as b
import alice_2 as a2

def main():
    """
    Main function to display options and execute corresponding actions based on user input.

    Options:
        A1  - Alice 1
        B   - Bob
        A2  - Alice 2

    Prompts the user to select an option and calls the appropriate function:
        - If "B" is selected, calls b.main()
        - If "A2" is selected, calls a2.main()
        - If "A" and "2" are both in the option, calls a2.main()
        - If "A" is selected, calls a1.main()
        - Otherwise, prints "Invalid option"
    """
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
