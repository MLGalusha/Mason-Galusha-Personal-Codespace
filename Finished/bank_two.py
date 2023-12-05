def main():
    x = convert_greeting(input("Greeting: "))
    print(f"${x}")


def convert_greeting(greeting):
    greeting = greeting.strip().lower().split()[0]
    if "hello" in greeting:
        return 0
    elif "h" in greeting[0]:
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()