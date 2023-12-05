def main():
    x = convert_lower(input("Input: "))
    print(f" shhh convert quiet...   {x}")


def convert_lower(word):
    word = word.lower()
    return word

if __name__ == "__main__":
    main()